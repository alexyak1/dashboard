#!/usr/bin/env bash

python execution/reg1.py
python execution/reg2.py
python execution/aod_hourly.py

python execution/health_checks.py
python execution/health_checks_lab.py

python execution/aod_daily.py
python execution/ml66_daily.py
python execution/swat_reg.py
