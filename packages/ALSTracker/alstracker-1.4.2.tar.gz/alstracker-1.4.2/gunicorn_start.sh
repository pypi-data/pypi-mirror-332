#!/bin/bash

RUN_DIR="XXX_RUN_DIR_XXX"
MINICONDA_DIR=XXX_MINIFORGE_XXX
USER=XXX_USER_XXX
GROUP=XXX_GROUP_XXX
export ALSTRACKER_MOGP=XXX_MOGP_PKL_XXX

cd $RUN_DIR

VENV=alstracker
NAME=ALS_Tracker
WORKERS=1
WORKER_CLASS=uvicorn.workers.UvicornWorker
BIND=unix:${RUN_DIR}/gunicorn.sock
LOG_LEVEL=error

source ${MINICONDA_DIR}/etc/profile.d/conda.sh
conda activate $VENV

exec gunicorn ALSTracker.main:app \
  --name "$NAME" \
  --workers "$WORKERS" \
  --worker-class "$WORKER_CLASS" \
  --user="$USER" \
  --group="$GROUP" \
  --bind="$BIND" \
  --log-level="$LOG_LEVEL" \
  --log-file=-
