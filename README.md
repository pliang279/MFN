# Memory-Fusion-Network
Code for Memory Fusion Network (MFN), AAAI 2018

This repository includes data, code and pretrained models for the AAAI 2018 paper, "Memory Fusion Network for Multi-view Sequential Learning"

Requirements:
Python 2.7 \n
PyTorch 0.4.0 \n
numpy 1.13.3 \n
sklearn 0.20.0

Data: we have included preprocessed data from the CMU-MOSI dataset for multimodal sentiment analysis. These are found in data/X_train.h5, data/y_train.h5 etc. To be consistent with previously reported results on the CMU-MOSI dataset, we used the exact same dataset as used in the baselines. We are in the process of integrate the model with the latest version of the CMU-MOSI and CMU-MOSEI datasets which can be found at https://github.com/A2Zadeh/CMU-MultimodalSDK/

Code: training code for both MFN and EF-LSTM (early fusion LSTM) are included in test_mosi.py

Pretrained models: pretrained MFN models optimized for MAE (Mean Absolute Error) and binary classification accuracy can be found in best/mfn_mae.pt, and best/mfn_acc.pt

You can run the code by typing "python test_mosi.py" in the command line. This loads the pretrained model best/mfn_mae.pt which gives a CMU-MOSI test set MAE of 0.954, and the pretrained model best/mfn_acc.pt which gives a CMU-MOSI test set binary classification accuracy of 77.4%.

Next steps: we are in the process of integrating the model with the latest version of the CMU-MOSI and CMU-MOSEI datasets which can be found at https://github.com/A2Zadeh/CMU-MultimodalSDK/

If you use this code, please cite our paper:

@article{zadeh2018memory, \n
  title={Memory Fusion Network for Multi-view Sequential Learning}, \n
  author={Zadeh, Amir and Liang, Paul Pu and Mazumder, Navonil and Poria, Soujanya and Cambria, Erik and Morency, Louis-Philippe}, \n
  journal={Proceedings of the Thirty-Second {AAAI} Conference on Artificial Intelligence}, \n
  year={2018} \n
}
