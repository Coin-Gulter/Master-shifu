import random
import time
import math
import cv2 as cv
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F

# program modules
from . import dt_set_module
from . import face_detection_module

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NET_WEIGHT = r'..\..\..\data\face_id_data\net_weight\net_model.pth'

round_tensor = lambda tensor, n_digits: torch.round(tensor * 10**n_digits) / (10**n_digits)
    
class user_detection_net(nn.Module):

    def __init__(self, mesh_size=956, transitive_size=57624, hidden_size=256, out_size=64):
        super(user_detection_net, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, 5, padding=2)
        self.conv2 = nn.Conv2d(6, 12, 3)
        self.conv3 = nn.Conv2d(12, 24, 2)
        self.transitive = nn.Linear(transitive_size, hidden_size*4)
        self.hidden1 = nn.Linear(hidden_size*4, hidden_size*2)
        self.hidden2 = nn.Linear(hidden_size*2, hidden_size)
        self.out = nn.Linear(hidden_size, out_size)

        self.relu = nn.ReLU()
        self.soft = nn.Softmax(dim=0)
        self.drop = nn.Dropout(p=0.2)

    def forward(self, inp_img):
        # print('inp_img_______________', inp_img.size())
        res_img = F.max_pool2d(self.conv1(inp_img), 2)
        # print('res_img1_______________', res_img.size())
        res_img = F.max_pool2d(self.conv2(res_img), 2)
        # print('res_img2_______________', res_img.size())
        res_img = F.max_pool2d(self.conv3(res_img), 2)
        # print('res_img3_______________', res_img.size())
        res_img = self.relu(torch.flatten(res_img))
        # print('res_flatten_______________', res_img.size())
        res = self.relu(self.transitive(res_img))
        # print('res1____________',res.size())
        res = self.drop(self.relu(self.hidden1(res)))
        # print('res2____________',res.size())
        res = self.relu(self.hidden2(res))
        # print('res3____________',res.size())
        out1 = self.soft(self.relu(self.out(res)))
        # print("outsoft____________", out1)
        out2 = self.out(res)
        # print("out____________", out2)
        return out1, out2


class net_train():
    def __init__(self, model, optimizer, criterion, face_dt_path, pretrained=False, path=NET_WEIGHT):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.pairs = None
        self.pretrained = pretrained
        self.path = path
        self.face_dt_path = face_dt_path
        self.status = None
        if pretrained:
            self.model.load_state_dict(torch.load(path))


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
        self.optimizer.zero_grad()

        res1, res2 = self.model(inp_img)
        #  print('criterion________', 'rezult1== ', res1, 'rezult2== ', res2, target)
        loss = self.criterion(res2, target)
        loss.backward()
        self.optimizer.step()

        tarv, tari = target.topk(1)
        topv, topi = res1.topk(1)
        print(f"Training_value = [{round(topv.item(), 2)}], Training_index = [{topi.item()}], Answear_index = [{tari.item()}], Answear = {'right' if tari == topi else 'wrong'}")

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
                self.pairs = dt_set_module.load_random_prepered_obj_from_dt_set(number=box, target_path= self.face_dt_path)
                print("__________New training object prepered")

            pair = random.choice(self.pairs)
            # cv.imshow('pair[0]', pair[0])
            # cv.waitKey(1)
            # print('pair___________', pair[0])
            input_img_tensor = torch.tensor(list(pair[0]), dtype=torch.float32, device=DEVICE, requires_grad=True).reshape(1, 400, 400)
            target_tensor = torch.tensor(pair[1], dtype=torch.float32, device=DEVICE).softmax(dim=0)
            #  print('tensor_______',input_tensor.size(), target_tensor.size())

            loss = self.train(input_img_tensor, target_tensor)
            print_loss_total += loss
            total_loss += loss

            if iter % print_every == 0:
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
        torch.save(self.model.state_dict(), self.path)

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
    model = user_detection_net(out_size=2)

    # preper_face_id_dt_set()

    # optimizer = optim.SGD(model.parameters(), lr=0.0001)
    # criterion = nn.CrossEntropyLoss()
    # training_net = net_train(model, optimizer=optimizer, criterion=criterion, pretrained=False)
    # training_net.train_iter(500)

    net_intro = net_use(model, NET_WEIGHT)

    # img = cv.imread(r'D:\Projects\PC_defender\data\filtered_face_dt\Volodymyr_Duleba\(0).jpg')
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # print(f"Object {img}")
    # value, index = net_intro.use(img)
    # print(f"Value = [{value}], Index = [{index}]")
    
    cap = cv.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    pTime = 0
    # old_face = np.array([0]*128)
    Fc_recog = face_detection_module.face_recognition()
    while True:
         success, img = cap.read()
         img = cv.flip(img, 1)
         img, detection = Fc_recog.faceDetector(img, False)
         img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
         if len(detection) != 0:
             face = detection[0][1]
             start_point_w = abs(face[0])
             start_point_h = abs(face[1])
             end_point_w = start_point_w + face[2]
             end_point_h = start_point_h + face[3]
             img = img[start_point_h:end_point_h, start_point_w:end_point_w]
             dsize = (400, 400)
             img = cv.resize(img, dsize, interpolation = cv.INTER_AREA)
            # print(face)
            # face = dimFrom2One(changeDimension(face))
            # face = changeDimension(face, 1)
            # print(face)
             value, index = net_intro.use(img)
             print(f"Value = [{value}], Index = [{index}]")
            #  right, wrong = compare_arr(old_face, face)
            #  print("Right answers_____", len(right))
            #  print("Wrong answers_____", len(wrong))
            #  old_face = face
            #  time.sleep(3)
            # value = getFromDict(FACE_DIRECTIONS_DICT, item)
            # print(value)
         #  img_tensor = torch.from_numpy(img).float()
         #  print(img_tensor)
         #  print(img_tensor.unsqueeze(0).unsqueeze(0))
         #  print(model(img_tensor.unsqueeze(0).unsqueeze(0)))
         cTime = time.time()
         fps = 1/(cTime-pTime)
         pTime = cTime
         cv.putText(img, f'fps: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
         cv.imshow('Image',img)
         cv.waitKey(1)
