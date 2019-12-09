import utils, waveglow_model
import DataLoader
from waveglow_model import WaveGlowLoss
from train_utils import get_test_loss_and_mse


dataset = DataLoader.DataLoader(test_f="./wind_power_data/wind_power_test.pickle", train_f="./wind_power_data/wind_power_train.pickle", rolling=True, small_subset=False, valid_split=.2, use_gpu=False)
criterion = WaveGlowLoss()
test_context, test_forecast = dataset.test_data()

context1 = torch.cuda.FloatTensor(test_context[i:i+96])
context2 = torch.cuda.FloatTensor(test_context[i+96:i+96*2])
context3 = torch.cuda.FloatTensor(test_context[i+96*2:i+96*3])
context4 = torch.cuda.FloatTensor(test_context[i+96*3:i+96*4])
context5 = torch.cuda.FloatTensor(test_context[i+96*4:i+96*5])
context6 = torch.cuda.FloatTensor(test_context[i+96*5:i+96*6])
context7 = torch.cuda.FloatTensor(test_context[i+96*6:i+96*7])
context8 = torch.cuda.FloatTensor(test_context[i+96*7:i+96*8])
context9 = torch.cuda.FloatTensor(test_context[i+96*8:i+96*9])
forecast1 = torch.cuda.FloatTensor(test_context[i+96:i+96+96])
forecast2 = torch.cuda.FloatTensor(test_context[i+96+96:i+96*2+96])
forecast3 = torch.cuda.FloatTensor(test_context[i+96*2+96:i+96*3+96])
forecast4 = torch.cuda.FloatTensor(test_context[i+96*3+96:i+96*4+96])
forecast5 = torch.cuda.FloatTensor(test_context[i+96*4+96:i+96*5+96])
forecast6 = torch.cuda.FloatTensor(test_context[i+96*5+96:i+96*6+96])
forecast7 = torch.cuda.FloatTensor(test_context[i+96*6+96:i+96*7+96])
forecast8 = torch.cuda.FloatTensor(test_context[i+96*7+96:i+96*8+96])
forecast9 = torch.cuda.FloatTensor(test_context[i+96*8+96:i+96*9+96])



model = waveglow_model.WaveGlow(
    n_context_channels=96, 
    n_flows=4, 
    n_group=12, 
    n_early_every=99,
    n_early_size=99,
    n_layers=8,
    dilation_list=[1,1,2,2,2,2,4,4],
    n_channels=96,
    kernel_size=3, use_cuda=True);

model, iteration_num = utils.load_checkpoint("./checkpoints/epoch-12_loss--0.3116", wg_model)
test_loss, test_mse = get_test_loss_and_mse(model, criterion, test_context, test_forecast, True)
print("Loss and MSE for model %s"% "waveglow_ncontextchannels-96_nflows-4_ngroup-12-nearlyevery-99-nearlysize-99-nlayers-8_dilations-1-1-2-2-2-2-4-4_nchannels_96-kernelsize-3-lr-0.00100_seed-2019")
print(test_loss)
print(test_mse)

for i in range(5):
	context1s.append(model.generate(context1).cpu())
	context2s.append(model.generate(context2).cpu()))
	context3s.append(model.generate(context3).cpu()))
	context4s.append(model.generate(context4).cpu()))
	context5s.append(model.generate(context5).cpu()))
	context6s.append(model.generate(context6).cpu()))
	context7s.append(model.generate(context7).cpu()))
	context8s.append(model.generate(context8).cpu()))
	context9s.append(model.generate(context9).cpu()))

# 5 models, 9 contexts, 5 generations per contex = 45 total


model = waveglow_model.WaveGlow(
    n_context_channels=96, 
    n_flows=4, 
    n_group=24, 
    n_early_every=99,
    n_early_size=99,
    n_layers=16,
    dilation_list=[1,1,2,2,2,2,2,2,2,2,2,2,2,2,4,4],
    n_channels=96,
    kernel_size=9, use_cuda=True);

model, iteration_num = utils.load_checkpoint("./checkpoints/epoch-19_loss--0.2139", wg_model)
test_loss, test_mse = get_test_loss_and_mse(model, criterion, test_context, test_forecast, True)
print("Loss and MSE for model %s"% "waveglow_ncontextchannels-96_nflows-4_ngroup-24-nearlyevery-99-nearlysize-99-nlayers-16_dilations-1-1-2-2-2-2-2-2-2-2-2-2-2-2-4-4_nchannels_96-kernelsize-9-lr-0.00100_seed-2019")
print(test_loss)
print(test_mse)

for i in range(5):
	context1s.append(model.generate(context1).cpu())
	context2s.append(model.generate(context2).cpu()))
	context3s.append(model.generate(context3).cpu()))
	context4s.append(model.generate(context4).cpu()))
	context5s.append(model.generate(context5).cpu()))
	context6s.append(model.generate(context6).cpu()))
	context7s.append(model.generate(context7).cpu()))
	context8s.append(model.generate(context8).cpu()))
	context9s.append(model.generate(context9).cpu()))


model = waveglow_model.WaveGlow(
    n_context_channels=96, 
    n_flows=16, 
    n_group=48, 
    n_early_every=99,
    n_early_size=99,
    n_layers=4,
    dilation_list=[1,1,2,2],
    n_channels=96,
    kernel_size=9, use_cuda=True);

model, iteration_num = utils.load_checkpoint("./checkpoints/epoch-22_loss--0.2237", wg_model)
test_loss, test_mse = get_test_loss_and_mse(model, criterion, test_context, test_forecast, True)
print("Loss and MSE for model %s"% "waveglow_ncontextchannels-96_nflows-4_ngroup-24-nearlyevery-99-nearlysize-99-nlayers-4_dilations-1-1-2-2_nchannels_96-kernelsize-9-lr-0.00100_seed-2019")
print(test_loss)
print(test_mse)

for i in range(5):
	context1s.append(model.generate(context1).cpu())
	context2s.append(model.generate(context2).cpu()))
	context3s.append(model.generate(context3).cpu()))
	context4s.append(model.generate(context4).cpu()))
	context5s.append(model.generate(context5).cpu()))
	context6s.append(model.generate(context6).cpu()))
	context7s.append(model.generate(context7).cpu()))
	context8s.append(model.generate(context8).cpu()))
	context9s.append(model.generate(context9).cpu()))


model = waveglow_model.WaveGlow(
    n_context_channels=96, 
    n_flows=16, 
    n_group=48, 
    n_early_every=99,
    n_early_size=99,
    n_layers=4,
    dilation_list=[1,1,2,2],
    n_channels=96,
    kernel_size=9, use_cuda=True);

model, iteration_num = utils.load_checkpoint("./checkpoints/epoch-36_loss—.1936", wg_model)
test_loss, test_mse = get_test_loss_and_mse(model, criterion, test_context, test_forecast, True)
print("Loss and MSE for model %s"% "waveglow_ncontextchannels-96_nflows-4_ngroup-24-nearlyevery-99-nearlysize-99-nlayers-4_dilations-1-1-2-2_nchannels_96-kernelsize-9-lr-0.00100_seed-2019")
print(test_loss)
print(test_mse)

for i in range(5):
	context1s.append(model.generate(context1).cpu())
	context2s.append(model.generate(context2).cpu()))
	context3s.append(model.generate(context3).cpu()))
	context4s.append(model.generate(context4).cpu()))
	context5s.append(model.generate(context5).cpu()))
	context6s.append(model.generate(context6).cpu()))
	context7s.append(model.generate(context7).cpu()))
	context8s.append(model.generate(context8).cpu()))
	context9s.append(model.generate(context9).cpu()))



model = waveglow_model.WaveGlow(
    n_context_channels=96, 
    n_flows=8, 
    n_group=24, 
    n_early_every=99,
    n_early_size=99,
    n_layers=8,
    dilation_list=[1,1,2,2,2,2,4,4],
    n_channels=96,
    kernel_size=9, use_cuda=True);

model, iteration_num = utils.load_checkpoint("./checkpoints/epoch_9_loss—.224", wg_model)
test_loss, test_mse = get_test_loss_and_mse(model, criterion, test_context, test_forecast, True)
print("Loss and MSE for model %s"% "waveglow_ncontextchannels-96_nflows-8_ngroup-24-nearlyevery-99-nearlysize-99-nlayers-8_dilations-1-1-2-2-2-2-4-4_nchannels_96-kernelsize-5-lr-0.00100_seed-2019")
print(test_loss)
print(test_mse)

for i in range(5):
	context1s.append(model.generate(context1).cpu())
	context2s.append(model.generate(context2).cpu()))
	context3s.append(model.generate(context3).cpu()))
	context4s.append(model.generate(context4).cpu()))
	context5s.append(model.generate(context5).cpu()))
	context6s.append(model.generate(context6).cpu()))
	context7s.append(model.generate(context7).cpu()))
	context8s.append(model.generate(context8).cpu()))
	context9s.append(model.generate(context9).cpu()))



context1s = np.savetxt('./context1.csv', np.vstack([[context1]+[forecast1]+context1s), delimiter=',')
context2s = np.savetxt('./context2.csv', np.vstack[context2]+[forecast2]+context2s), delimiter=',')
context3s = np.savetxt('./context3.csv', np.vstack([context3]+[forecast3]+context3s), delimiter=',')
context4s = np.savetxt('./context4.csv', np.vstack([context4]+[forecast4]+context4s), delimiter=',')
context5s = np.savetxt('./context5.csv', np.vstack([context5]+[forecast5]+context5s), delimiter=',')
context6s = np.savetxt('./context6.csv', np.vstack([context6]+[forecast6]+context6s), delimiter=',')
context7s = np.savetxt('./context7.csv', np.vstack([context7]+[forecast7]+context7s), delimiter=',')
context8s = np.savetxt('./context8.csv', np.vstack([context8]+[forecast8]+context8s), delimiter=',')
context9s = np.savetxt('./context9.csv', np.vstack([context9]+[forecast9]+context9s), delimiter=',')


