#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python downstream/run_downstream.py \
    --savedir './csv_logs' \
    --model 'electra' \
    --task "mimic-mortality" \
    --data_dir './data/downstream' \
    --data_filename 'mimic.csv' \
    --epochs 3 \
    --lr 2e-6 \
    --use_scheduler \
    -bs 8 \
    --save_every 1 \
    --dropout 0.1 \
    --rnn_layers 3 \
    --da_layers 1 \
    --hidden_size 512 \
    --eval_every 10000 \
    --pretrained_model './models/electra.pt'
    #--diag_to_idx_path "path to diag_to_idx file" \
    #--embs_path "path to pretrained fasttext embeddings" \