import random
import time
import math
import os
import cv2 as cv
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import string
import unicodedata

# program modules
import dt_set_module_test2

PATH_NOW = os.getcwd()
print('path_now___', PATH_NOW)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NET_ANALYZER_WEIGHT = PATH_NOW + r'\program\data\face_id_data\net_weight\net_1_model.pth'
NET_IMG_COMPRESSION_WEIGHT = PATH_NOW + r'\program\data\face_id_data\net_weight\net_2_model.pth'
NET_PASS_GETTING_WEIGHT = PATH_NOW + r'\program\data\face_id_data\net_weight\net_3_model.pth'
FACE_JSON_TARGET_PATH = PATH_NOW + r'\program\data\face_id_data\target_json\face_id_target_2.json'
FACE_JSON_TARGET_PASS_PATH = PATH_NOW + r'\program\data\face_id_data\target_json\face_pass_target_2.json'
FACE_VALIDATE_DTSET =  PATH_NOW + r'\program\data\face_id_data\validate_face_dt'


CHARACTERS_NUMBER = 129
CLIENT_NUMBER = 2
HIDDEN_SIZE = 256

round_tensor = lambda tensor, n_digits: torch.round(tensor * 10**n_digits) / (10**n_digits)

class img_compression_net(nn.Module):

    def __init__(self, transitive_size=108300, out_size=HIDDEN_SIZE):
        super(img_compression_net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 10)
        # self.conv2 = nn.Conv2d(6, 12, 4)
        self.conv3 = nn.Conv2d(6, 12, 5)
        # self.transitive = nn.Linear(transitive_size, hidden_size*4)
        self.hidden1 = nn.Linear(transitive_size, out_size)

        self.relu = nn.ReLU()
        self.drop = nn.Dropout(p=0.2)

    def forward(self, img):
        # print('inp_img_______________', inp_img.size())
        res = F.max_pool2d(self.conv1(img), 2)
        # print('res_img1_______________', res_img.size())
        res = F.max_pool2d(self.conv3(res), 2)
        # print('res_img3_______________', res_img.size())
        res = torch.flatten(res)
        # print('res_flatten_______________', res_img[:5])
        res = self.relu(self.drop(self.hidden1(res)))
        # print('res1____________',res[:5])
        return res
    
class user_analyzer_net(nn.Module):

    def __init__(self, hidden_size=HIDDEN_SIZE, out_size=2):
        super(user_analyzer_net, self).__init__()

        self.input = nn.Linear(hidden_size, hidden_size)
        self.hidden1 = nn.Linear(hidden_size, hidden_size*2)
        self.hidden2 = nn.Linear(hidden_size*2, hidden_size)
        self.out = nn.Linear(hidden_size, out_size)

        self.relu = nn.ReLU()
        self.soft = nn.LogSoftmax(dim=0)

    def forward(self, inp):
        res = self.relu(self.input(inp))
        # print('res2____________',res[:5])
        hidden1 = self.relu(self.hidden1(res))
        # print('hidden_________', hidden[:5])
        hidden2 = self.relu(self.hidden2(hidden1))
        # print("hidden2_________", hidden2[:5])
        out = self.soft(self.out(hidden2))
        # print("outsoft____________", out1[:5])
        return out

class password_getting_net(nn.Module):

    def __init__(self, input_size=2, hidden_size=HIDDEN_SIZE, out_size=CHARACTERS_NUMBER):
        super(password_getting_net, self).__init__()

        self.input = nn.Linear(input_size, hidden_size)
        self.conecting = nn.Linear(hidden_size*2, hidden_size*2)
        self.hidden = nn.Linear(hidden_size*2, hidden_size)
        self.i2o = nn.Linear(hidden_size, out_size)
        self.i2h = nn.Linear(hidden_size, hidden_size)

        self.relu = nn.ReLU()
        self.soft = nn.LogSoftmax(dim=0)

    def forward(self, inp, next_hidden):
        # print('pass net input__________', inp.size())
        # print('pass net next hidden__________', next_hidden.size())
        hidden = self.input(inp)
        # print('input hidden____________', inp_hidden[:5])
        hidden1 = self.conecting(torch.cat((hidden, next_hidden), dim=0))
        hidden2 = self.relu(self.hidden(hidden1))
        # print('res2____________',res[:5])
        next_hidden = self.relu(self.i2h(hidden2))
        # print('hidden_________', hidden[:5])
        out = self.soft(self.i2o(hidden2))
        # print("outsoft____________", out1[:5])
        return out, next_hidden

class net_recognize_train():
    def __init__(self, model_analyzer, model_img_compression, optimizer2analyzer, optimizer2img_compression, criterion, face_dt_path=FACE_JSON_TARGET_PATH, pretrained=False, path2analyzer=NET_ANALYZER_WEIGHT, path2img_compression=NET_IMG_COMPRESSION_WEIGHT):
        self.model_analyzer = model_analyzer
        self.model_img_compression = model_img_compression
        self.optimizer2analyzer = optimizer2analyzer
        self.optimizer2img_compression =optimizer2img_compression
        self.criterion = criterion
        self.pairs = None
        self.pretrained = pretrained
        self.path2analyzer = path2analyzer
        self.path2img_compression = path2img_compression
        self.face_dt_path = face_dt_path

        if pretrained:
            self.model_analyzer.load_state_dict(torch.load(self.path2analyzer))
            self.model_img_compression.load_state_dict(torch.load(self.path2img_compression))

    def number2tensor(self, number, number2long_tensor=None, dtype= torch.float32):
        if number2long_tensor:
            zero_tensor = torch.zeros(number2long_tensor, dtype=dtype, device=DEVICE)
            zero_tensor[number] = 1
            return zero_tensor
        else:
            return torch.tensor(number)

    def tensor2number(self, tensor):
        tensor.tolist()
        return tensor.index(1)

    def target2tensor(self, target, elements_number2long_tensor=None, dtype=torch.float32):
        tensor_list = []
        for number in target:
            tensor_list.append(self.number2tensor(number, elements_number2long_tensor, dtype))
        return tensor_list

    def asMinutes(self, s):
        m = math.floor(s / 60)
        s -= m * 60
        return '%dm %ds' % (m, s)

    def timeSince(self, since, percent):
        now = time.time()
        s = now - since
        es = s / (percent)
        rs = es - s
        return '%s (- %s)' % (self.asMinutes(s), self.asMinutes(rs))

    def train(self, inp_img, target_client):
        self.optimizer2analyzer.zero_grad()
        self.optimizer2img_compression.zero_grad()
        loss = 0
        # print('target_____________', target)

        img_compression = self.model_img_compression(inp_img)
        res = self.model_analyzer(img_compression)
        print('criterion________ rezult1== ', torch.exp(res), 'target== ', target_client)
        loss += self.criterion(res, target_client)

        loss.backward()
        self.optimizer2analyzer.step()
        self.optimizer2img_compression.step()

        return loss

    def train_iter(self, n_iter=1500, box=100, print_every=10, plot_every=10):
        start = time.time()
        print_loss_total = 0
        # all_losses = []
        # total_loss = 0
        result_list = []

        
        torch.enable_grad()

        for iter in range(1, n_iter+1):

            if (self.pairs == None) or (iter%box == 0):
                print("Prepare new training object___________")
                self.pairs = dt_set_module_test2.load_random_prepered_obj_from_recognize_dt_set(number=box, target_path=self.face_dt_path)
                print("__________New training object prepered")

            pair = random.choice(self.pairs)
            # print('pair___________', pair[0])
            input_tensor = torch.tensor(list(pair[0]), dtype=torch.float32, device=DEVICE, requires_grad=True).reshape(1, 400, 400)
            # target_tensor = torch.tensor(pair[1], dtype=torch.long, device=DEVICE)
            target_tensor = torch.tensor(pair[1][0], dtype=torch.long, device=DEVICE)
            # print('tensor_______',input_img_tensor.size(), target_tensor)
            # print('target_______', target_tensor)

            loss = self.train(input_tensor, target_tensor)
            print_loss_total += loss

            if iter % print_every == 0:
                # print('loss total______', print_loss_total)
                print_loss_avg = print_loss_total / print_every
                # print_loss_total = 0
                self.status = iter/n_iter * 100
                res_str = 'img str - %s (%d %d%%) %.4f' % (self.timeSince(start, iter / n_iter),
                                             iter, self.status, print_loss_avg)
                
                print_loss_total = 0
                print(res_str)
                result_list.append(res_str)
                time.sleep(2)

            # if iter % plot_every == 0:
            #     all_losses.append(total_loss / plot_every)
            #     total_loss = 0

        torch.save(self.model_analyzer.state_dict(), self.path2analyzer)
        torch.save(self.model_img_compression.state_dict(), self.path2img_compression)

        print(result_list)
        # plt.figure()
        # plt.plot(all_losses)
        # plt.show()
        return 1
    
    def validate(self, number):
        number_of_recognizes = 0
        torch.no_grad()

        for _ in range(number):
            rezult = []
            image = None
            who_is_on_img = None

            folders = os.listdir(FACE_VALIDATE_DTSET) 
            work_folder = random.choice(folders)
            if work_folder == 'client':
                who_is_on_img = 1
            else:
                who_is_on_img = 0

            random_folder_path = os.path.join(FACE_VALIDATE_DTSET, work_folder)
            random_img_path = os.path.join(random_folder_path, random.choice(os.listdir(random_folder_path)))

            image = cv.imread(random_img_path, cv.IMREAD_GRAYSCALE)
            image_tensor = torch.tensor(image, dtype=torch.float32, device=DEVICE, requires_grad=True).reshape(1, 400, 400)

            img_compression = self.model_img_compression(image_tensor)
            res_who_is = self.model_analyzer(img_compression)
            topv, topi_recog = res_who_is.topk(1)
            # print('Rezult who is there______ predicted = ', topi_recog.item(), 'real = ', who_is_on_img)

            if topi_recog.item() == who_is_on_img:
                number_of_recognizes += 1

            print('End of iteration rezult = ', rezult)
        print('percentage of validate people = ', (number_of_recognizes/number*100))


class net_pass_getting_train():
    def __init__(self, model_password_getting, optimizer2password_getting, criterion, face_dt_path=FACE_JSON_TARGET_PASS_PATH, pretrained=False, path2password_getting=NET_PASS_GETTING_WEIGHT, hidden_size=HIDDEN_SIZE):
        self.model_password_getting = model_password_getting
        self.optimizer2password_getting = optimizer2password_getting
        self.criterion = criterion
        self.pairs = None
        self.hidden_size = hidden_size
        self.pretrained = pretrained
        self.path2password_getting = path2password_getting
        self.face_dt_path = face_dt_path

        if pretrained:
            self.model_password_getting.load_state_dict(torch.load(self.path2password_getting))

    def init_hidden(self):
        return  torch.zeros(self.hidden_size)

    def number2tensor(self, number, number2long_tensor=None, dtype= torch.float32):
        if number2long_tensor:
            zero_tensor = torch.zeros(number2long_tensor, dtype=dtype, device=DEVICE)
            zero_tensor[number] = 1
            return zero_tensor
        else:
            return torch.tensor(number)

    def tensor2number(self, tensor):
        tensor.tolist()
        return tensor.index(1)

    def target2tensor(self, target, elements_number2long_tensor=None, dtype=torch.float32):
        tensor_list = []
        for number in target:
            tensor_list.append(self.number2tensor(number, elements_number2long_tensor, dtype))
        return tensor_list
    
    def make_zero_one_tensor(self, number, length, dtype=torch.float32):
        zeros_tensor = torch.zeros(length, dtype=dtype, device=DEVICE)
        zeros_tensor[int(number)] = 1
        return zeros_tensor

    def asMinutes(self, s):
        m = math.floor(s / 60)
        s -= m * 60
        return '%dm %ds' % (m, s)

    def timeSince(self, since, percent):
        now = time.time()
        s = now - since
        es = s / (percent)
        rs = es - s
        return '%s (- %s)' % (self.asMinutes(s), self.asMinutes(rs))

    def train(self, inp_pass, target_pass):
        self.optimizer2password_getting.zero_grad()
        next_hidden = self.init_hidden()
        loss = 0
        rezult = []
        # print('target_____________', target)

        for targ_elem in target_pass:
            res, next_hidden = self.model_password_getting(inp_pass, next_hidden)
            loss += self.criterion(res, targ_elem)

            # res = torch.exp(res)
            topv, topi = res.topk(1)
            # tarv, tari = targ_elem.topk(1)
            # print('criterion________', 'rezult1== ', torch.exp(topv), topi, 'target== ', targ_elem)
            # print(f"Training_value = [{round(topv.item(), 2)}], Training_index = [{topi.item()}]")
            # print('res_________', res[:10])

            rezult.append(chr(topi.item()))
            # targ.append(chr(tari.item()))
            # num_rezult.append(topi.item())

            # loss.backward()
            # self.optimizer.step()

        loss.backward()
        self.optimizer2password_getting.step()

        # print('loss______________', loss)
        print('train _____________ result=', rezult)
        # print('train target_________', targ)
        # print('train number result_________', num_rezult)
        # topv, topi = res1.topk(1)
        # print(f"Training_value = [{round(topv.item(), 2)}], Training_index = [{topi.item()}], Answear_index = [{tari.item()}], Answear = {'right' if tari == topi else 'wrong'}")

        return loss

    def train_iter(self, n_iter=1500, box=100, print_every=10, plot_every=10):
        start = time.time()
        print_loss_total = 0
        # all_losses = []
        # total_loss = 0
        result_list = []

        
        torch.enable_grad()

        for iter in range(1, n_iter+1):

            if (self.pairs == None) or (iter%box == 0):
                print("Prepare new training object___________")
                self.pairs = dt_set_module_test2.load_random_prepered_obj_from_password_dt_set(number=box, target_path=self.face_dt_path)
                print("__________New training object prepered")

            pair = random.choice(self.pairs)
            # print('pass pair___________', pair)
            input_tensor = self.make_zero_one_tensor(pair[0], CLIENT_NUMBER)
            # print('tensor input pass_______', input_tensor)
            target_tensor = self.target2tensor(pair[1], dtype=torch.long)
            # print('tensor target pass_______',target_tensor)

            loss = self.train(input_tensor, target_tensor)
            print_loss_total += loss
            # total_loss += loss

            if iter % print_every == 0:
                # print('loss total______', print_loss_total)
                print_loss_avg = print_loss_total / print_every
                # print_loss_total = 0
                self.status = iter/n_iter * 100
                res_str = 'pass str - %s (%d %d%%) %.4f' % (self.timeSince(start, iter / n_iter),
                                             iter, self.status, print_loss_avg)
                print_loss_total = 0
                print(res_str)
                result_list.append(res_str)
                time.sleep(2)

            # if iter % plot_every == 0:
            #     all_losses.append(total_loss / plot_every)
            #     total_loss = 0

        torch.save(self.model_password_getting.state_dict(), self.path2password_getting)

        print(result_list)
        # plt.figure()
        # plt.plot(all_losses)
        # plt.show()
        return 1
    
    def validate(self, number):
        torch.no_grad()
        for _ in range(number):
            rezult = []
            topi = None
            inside_iter = 0
            next_hidden = self.init_hidden()
            input_list = [0,0]

            input_list[random.randint(0,1)] = 1

            input_tensor = torch.tensor(input_list, dtype=torch.float32, device=DEVICE, requires_grad=False)

            while topi != 128 and inside_iter <= 20:
                symbol, next_hidden = self.model_password_getting(input_tensor, next_hidden)
                topv, topi = symbol.topk(1)

                rezult.append(chr(topi.item()))
                inside_iter += 1

            # print('End of iteration rezult = ', rezult, 'who is this = ', input_tensor)s


class net_use():

    def __init__(self, model, state_dict_file):
        self.model = model
        self.model.load_state_dict(torch.load(state_dict_file))

    def use(self, inp):
        inp = torch.tensor(list(inp), dtype=torch.float32, device=DEVICE).reshape(1, 400, 400)
        res1, res2 = self.model(inp)
        # topv, topi = res1.topk(1)
        # res2 = torch.round(res1)
        topv, topi = res1.topk(1)
        # res2 = res2.detach().numpy()
        # print('items______', res2)
        return topv.item(), topi.item()


if __name__ == '__main__':
    model_analyzer = user_analyzer_net()
    model_img_compression = img_compression_net()
    model_pass_getting = password_getting_net()

    dt_set_module_test2.preper_face_id_target_dt_set('jenet')

    optimizer2analyzer = optim.Adam(model_analyzer.parameters(), lr=0.0001)
    optimizer2img_compression = optim.Adam(model_img_compression.parameters(), lr=0.0001)
    optimizer2pass_getting = optim.Adam(model_pass_getting.parameters(), lr=0.0001)
    criterion = nn.NLLLoss()


    training_recog_net = net_recognize_train(model_analyzer, model_img_compression, optimizer2analyzer=optimizer2analyzer
                            ,optimizer2img_compression=optimizer2img_compression, criterion=criterion, pretrained=False)
    training_recog_net.train_iter(2000)
    training_recog_net.validate(1000)

    # training_pass_getter_net = net_pass_getting_train(model_pass_getting, optimizer2pass_getting, criterion, pretrained=False)
    # training_pass_getter_net.train_iter(1000, print_every=100)
    # training_pass_getter_net.validate(10)


    # net_intro = net_use(model, NET_WEIGHT)

    # img = cv.imread(r'D:\Projects\PC_defender\data\filtered_face_dt\Volodymyr_Duleba\(0).jpg')
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # print(f"Object {img}")
    # value, index = net_intro.use(img)
    # print(f"Value = [{value}], Index = [{index}]")
    
    # cap = cv.VideoCapture(0)
    # cap.set(3, 1280)
    # cap.set(4, 720)
    # pTime = 0
    # # old_face = np.array([0]*128)
    # Fc_recog = face_detection_module.face_recognition()
    # while True:
    #      success, img = cap.read()
    #      img = cv.flip(img, 1)
    #      img, detection = Fc_recog.faceDetector(img, False)
    #      img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #      if len(detection) != 0:
    #          face = detection[0][1]
    #          start_point_w = abs(face[0])
    #          start_point_h = abs(face[1])
    #          end_point_w = start_point_w + face[2]
    #          end_point_h = start_point_h + face[3]
    #          img = img[start_point_h:end_point_h, start_point_w:end_point_w]
    #          dsize = (400, 400)
    #          img = cv.resize(img, dsize, interpolation = cv.INTER_AREA)
    #         # print(face)
    #         # face = dimFrom2One(changeDimension(face))
    #         # face = changeDimension(face, 1)
    #         # print(face)
    #          value, index = net_intro.use(img)
    #          print(f"Value = [{value}], Index = [{index}]")
    #         #  right, wrong = compare_arr(old_face, face)
    #         #  print("Right answers_____", len(right))
    #         #  print("Wrong answers_____", len(wrong))
    #         #  old_face = face
    #         #  time.sleep(3)
    #         # value = getFromDict(FACE_DIRECTIONS_DICT, item)
    #         # print(value)
    #      #  img_tensor = torch.from_numpy(img).float()
    #      #  print(img_tensor)
    #      #  print(img_tensor.unsqueeze(0).unsqueeze(0))
    #      #  print(model(img_tensor.unsqueeze(0).unsqueeze(0)))
    #      cTime = time.time()
    #      fps = 1/(cTime-pTime)
    #      pTime = cTime
    #      cv.putText(img, f'fps: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    #      cv.imshow('Image',img)
    #      cv.waitKey(1)
