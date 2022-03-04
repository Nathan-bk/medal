#!/bin/bash

CUDA_VISIBLE_DEVICES=0,1 python run.py \
    --savedir './run_logs' \
    --model 'electra' \
    --data_dir './data' \
    --adam_path './toy_data/valid_adam.txt' \
    --embs_path './data' \
    --data_filename 'medal.csv' \
    --epochs 10 \
    --lr 2e-6 \
    --use_scheduler \
    -bs 8 \
    --save_every 1 \
    --dropout 0.1 \
    --rnn_layers 3 \
    --da_layers 1 \
    --hidden_size 512 \
    --eval_every 200000 \
    # --pretrained_model "path to pretrained model"
    # Model options : rnn, rnnsoft, electra 