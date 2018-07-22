#!/bin/sh

abs_builddir="/home/cosailer/projects/aircrack-ng-1.3/test"; export abs_builddir
abs_srcdir="/home/cosailer/projects/aircrack-ng-1.3/test"; export abs_srcdir
top_builddir=".."; export top_builddir
top_srcdir=".."; export top_srcdir

EXEEXT=""; export EXEEXT

AIRCRACK_LIBEXEC_PATH="/home/cosailer/projects/aircrack-ng-1.3/src"; export AIRCRACK_LIBEXEC_PATH

AIRCRACK_NG_ARGS="${AIRCRACK_NG_ARGS:--p 96}"; export AIRCRACK_NG_ARGS
