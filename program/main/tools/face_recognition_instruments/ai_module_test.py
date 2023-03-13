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
import dt_set_module_test

print('path_now___', os.getcwd())
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NET_ANALYZER_WEIGHT = r'data\face_id_data\net_weight\net_1_model.pth'
NET_IMG_COMPRESSION_WEIGHT = r'data\face_id_data\net_weight\net_2_model.pth'
FACE_JSON_TARGET_PATH = r'data\face_id_data_test\target_json\face_id_target_test.json'
CHARACTERS_NUMBER = 129

round_tensor = lambda tensor, n_digits: torch.round(tensor * 10**n_digits) / (10**n_digits)

class img_compression_net(nn.Module):

    def __init__(self, transitive_size=108300, out_size=512):
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

    def __init__(self, hidden_size=512, out_size=CHARACTERS_NUMBER):
        super(user_analyzer_net, self).__init__()

        self.hidden2 = nn.Linear(hidden_size*2, hidden_size)
        self.i2o = nn.Linear(hidden_size, out_size)
        self.i2h = nn.Linear(hidden_size, hidden_size)
        self.h2i = nn.Linear(hidden_size, hidden_size)

        self.relu = nn.ReLU()
        self.soft = nn.LogSoftmax(dim=0)

    def forward(self, inp, next_hidden):
        hidden = self.relu(self.h2i(next_hidden))
        # print('input hidden____________', inp_hidden[:5])
        res = self.relu(self.hidden2(torch.cat((inp, hidden), dim=0)))
        # print('res2____________',res[:5])
        hidden = self.relu(self.i2h(res))
        # print('hidden_________', hidden[:5])
        out1 = self.soft(self.i2o(res))
        # print("outsoft____________", out1[:5])
        return out1, hidden


class net_train():
    def __init__(self, model_analyzer, model_img_compression, optimizer2analyzer, optimizer2img_compression, criterion, face_dt_path=FACE_JSON_TARGET_PATH, pretrained=False, path2analyzer=NET_ANALYZER_WEIGHT, path2img_compression=NET_IMG_COMPRESSION_WEIGHT, hidden_size=512):
        self.model_analyzer = model_analyzer
        self.model_img_compression = model_img_compression
        self.optimizer2analyzer = optimizer2analyzer
        self.optimizer2img_compression =optimizer2img_compression
        self.criterion = criterion
        self.pairs = None
        self.hidden_size = hidden_size
        self.pretrained = pretrained
        self.path2analyzer = path2analyzer
        self.path2img_compression = path2img_compression
        self.face_dt_path = face_dt_path
        self.status = None

        if pretrained:
            self.model_analyzer.load_state_dict(torch.load(self.path2analyzer))
            self.model_img_compression.load_state_dict(torch.load(self.path2img_compression))

    def init_hidden(self):
        return  torch.zeros(self.hidden_size)

    def number2tensor(self, number):
        # zero_tensor = torch.zeros(CHARACTERS_NUMBER, dtype=torch.long, device=DEVICE)
        # zero_tensor[number] = 1
        return torch.tensor(number)

    def tensor2number(self, tensor):
        tensor.tolist()
        return tensor.index(1)

    def target2tensor(self, target):
        tensor_list = []
        for number in target:
            tensor_list.append(self.number2tensor(number))
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

    def train(self, inp_img, target):
        self.optimizer2analyzer.zero_grad()
        self.optimizer2img_compression.zero_grad()
        next_hidden = self.init_hidden()
        loss = 0
        rezult = []
        targ = []
        num_rezult = []
        # print('target_____________', target)

        img_compression = self.model_img_compression(inp_img)

        for targ_elem in target:
            res, next_hidden = self.model_analyzer(img_compression, next_hidden)
            # print('criterion________', 'rezult1== ', res1, 'target== ', targ_elem)
            loss += self.criterion(res, targ_elem)

            # res = torch.exp(res)
            topv, topi = res.topk(1)
            # tarv, tari = targ_elem.topk(1)
            # print(f"Training_value = [{round(topv.item(), 2)}], Training_index = [{topi.item()}]")
            # print('res_________', res[:10])

            rezult.append(chr(topi.item()))
            # targ.append(chr(tari.item()))
            # num_rezult.append(topi.item())

            # loss.backward()
            # self.optimizer.step()

        loss.backward()
        self.optimizer2analyzer.step()
        self.optimizer2img_compression.step()

        # print('loss______________', loss)
        print('train result_________', rezult)
        # print('train target_________', targ)
        # print('train number result_________', num_rezult)
        # topv, topi = res1.topk(1)
        # print(f"Training_value = [{round(topv.item(), 2)}], Training_index = [{topi.item()}], Answear_index = [{tari.item()}], Answear = {'right' if tari == topi else 'wrong'}")

        return loss

    def train_iter(self, n_iter=1500, box=100, print_every=10, plot_every=10):
        start = time.time()
        print_loss_total = 0
        all_losses = []
        total_loss = 0
        result_list = []

        
        torch.enable_grad()

        for iter in range(1, n_iter+1):

            if (self.pairs == None) or (iter%box == 0):
                print("Prepare new training object___________")
                self.pairs = dt_set_module_test.load_random_prepered_obj_from_dt_set(number=box, target_path=self.face_dt_path)
                print("__________New training object prepered")

            pair = random.choice(self.pairs)
            # cv.imshow('pair[0]', pair[0])
            # cv.waitKey(1)
            # print('pair___________', pair[0])
            input_img_tensor = torch.tensor(list(pair[0]), dtype=torch.float32, device=DEVICE, requires_grad=True).reshape(1, 400, 400)
            # target_tensor = torch.tensor(pair[1], dtype=torch.long, device=DEVICE)
            target_tensor = self.target2tensor(pair[1])
            # print('tensor_______',input_img_tensor.size(), target_tensor)
            # print('target_______', target_tensor)

            loss = self.train(input_img_tensor, target_tensor)
            print_loss_total += loss
            total_loss += loss

            if iter % print_every == 0:
                # print('loss total______', print_loss_total)
                print_loss_avg = print_loss_total / print_every
                print_loss_total = 0
                self.status = iter/n_iter * 100
                res_str = '%s (%d %d%%) %.4f' % (self.timeSince(start, iter / n_iter),
                                             iter, self.status, print_loss_avg)
                print(res_str)
                result_list.append(res_str)

            if iter % plot_every == 0:
                all_losses.append(total_loss / plot_every)
                total_loss = 0

        self.status = 100
        torch.save(self.model_analyzer.state_dict(), self.path2analyzer)
        torch.save(self.model_img_compression.state_dict(), self.path2img_compression)

        print(result_list)
        # plt.figure()
        # plt.plot(all_losses)
        # plt.show()
        return 1




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

    dt_set_module_test.preper_face_id_target_dt_set('jeneteyruinpckspaqew')

    optimizer2analyzer = optim.Adam(model_analyzer.parameters(), lr=0.0001)
    optimizer2img_compression = optim.Adam(model_img_compression.parameters(), lr=0.001)
    criterion = nn.NLLLoss()
    training_net = net_train(model_analyzer, model_img_compression, optimizer2analyzer=optimizer2analyzer
                            ,optimizer2img_compression=optimizer2img_compression, criterion=criterion, pretrained=False)
    training_net.train_iter(5000)

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
