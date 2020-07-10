# Lint as: python2, python3
# Copyright 2020 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
r"""Ground truth values for `german_credit_numeric_sparse_logistic_regression`.

Automatically generated using the command:

```
bazel run //tools/inference_gym_ground_truth:get_ground_truth --   --target \
  german_credit_numeric_sparse_logistic_regression \
```
"""

import numpy as onp

IDENTITY_GLOBAL_SCALE_MEAN = onp.array([
    0.34659073894573333,
]).reshape(())

IDENTITY_GLOBAL_SCALE_MEAN_STANDARD_ERROR = onp.array([
    0.000272747852246003,
]).reshape(())

IDENTITY_GLOBAL_SCALE_STANDARD_DEVIATION = onp.array([
    0.14724073850406091,
]).reshape(())

IDENTITY_LOCAL_SCALES_MEAN = onp.array([
    2.463490300452,
    1.7887786041154636,
    1.6563136083116041,
    0.5519206650013805,
    1.5394545573813851,
    0.7599606084736111,
    0.7036570767876855,
    0.34192755997796453,
    0.8286448399568738,
    0.5402315320427129,
    0.9941377814297162,
    0.4659435118222056,
    0.33472227702343293,
    0.4668665248953582,
    1.113833174907365,
    1.2484654947130802,
    1.2493555032449397,
    0.9002762576097485,
    0.8203564777953762,
    0.6220675657487186,
    0.587131989296038,
    0.3675478248197654,
    0.3520805568170539,
    0.3487802931745999,
    3.292519992277333,
]).reshape((25,))

IDENTITY_LOCAL_SCALES_MEAN_STANDARD_ERROR = onp.array([
    0.0017641741059706785,
    0.001516481607275699,
    0.0014242773672903586,
    0.0008579150964574504,
    0.0013329372074654179,
    0.0010130506561244607,
    0.0011522660104074439,
    0.0005879308709578674,
    0.0010893085655107758,
    0.0008167446420001881,
    0.0011984325674918583,
    0.0007336864593479592,
    0.0006211324724363598,
    0.0007670407051219993,
    0.0011291594669008444,
    0.00132339168370259,
    0.0012121901593444755,
    0.001325457511808573,
    0.0011999294770858625,
    0.0009436277957373772,
    0.0009918323254916514,
    0.0006772923776325724,
    0.0006017346821746667,
    0.0006597407581035223,
    0.0024768287640381365,
]).reshape((25,))

IDENTITY_LOCAL_SCALES_STANDARD_DEVIATION = onp.array([
    1.5075580945641331,
    1.2975451119708046,
    1.2403744545574242,
    0.8109212176893325,
    1.2017203939838057,
    0.9209422933171497,
    0.8883342326667965,
    0.6175284169764399,
    0.9706829079457918,
    0.7916410671136468,
    1.005396724253933,
    0.732851666032709,
    0.6102617912853542,
    0.7344511884032239,
    1.0885623239562547,
    1.1023481683516345,
    1.1185932871836974,
    1.017937077172275,
    0.9758624437458842,
    0.8576356673961744,
    0.8428188964409719,
    0.6418237106325464,
    0.6255463521936968,
    0.6264242084011953,
    1.76745245577102,
]).reshape((25,))

IDENTITY_UNSCALED_WEIGHTS_MEAN = onp.array([
    -1.1874458820754,
    1.0384645828471206,
    -1.0074514397470067,
    0.3996121094094093,
    -0.9775622638665891,
    -0.6347101815984167,
    -0.6060772178490221,
    0.005007324596130749,
    0.6613495805635855,
    -0.42657011850738913,
    -0.7953333872644853,
    0.3316809760062276,
    0.047962915272461194,
    -0.34821728718139444,
    -0.8173524833666775,
    0.8953628068368229,
    -0.883460994450207,
    0.6783476963022333,
    0.627839906838241,
    0.461082669686665,
    -0.3947033582018714,
    -0.19014940758697838,
    -0.02970321605348583,
    0.002136334926435367,
    -1.3463701543726667,
]).reshape((25,))

IDENTITY_UNSCALED_WEIGHTS_MEAN_STANDARD_ERROR = onp.array([
    0.0006457753961080904,
    0.0006674023934676173,
    0.0006738618500988743,
    0.0008203078961481262,
    0.0006615226355702643,
    0.0008300165860650571,
    0.0008763573896004647,
    0.0007808956077132443,
    0.0008102310499895648,
    0.0008079303904521567,
    0.0007498558266850107,
    0.0008140708153511056,
    0.0008046280805054354,
    0.0008147061773258081,
    0.0007370835556863866,
    0.0006819523146885135,
    0.0006980473714010189,
    0.0009173185279213508,
    0.0009470781973364478,
    0.0008872424075845784,
    0.0008596410801932306,
    0.0007783035016121979,
    0.0008054381422493456,
    0.0007817056326528812,
    0.0007046867365556592,
]).reshape((25,))

IDENTITY_UNSCALED_WEIGHTS_STANDARD_DEVIATION = onp.array([
    0.5688351286680584,
    0.564794723184628,
    0.5613200675358188,
    0.7844719964230911,
    0.5612084798495387,
    0.692000644322665,
    0.6955933031622102,
    0.8178381849451496,
    0.6897213537621227,
    0.7675438129083711,
    0.6044553106279033,
    0.7889826757600257,
    0.8166580422210814,
    0.7828086978506955,
    0.6213492655897788,
    0.5688067799197392,
    0.5873284385399956,
    0.6999181235546609,
    0.7208029402399017,
    0.7749054165406737,
    0.794863854895619,
    0.8054775576861729,
    0.8237111043591746,
    0.8221311381497441,
    0.5773283660916191,
]).reshape((25,))
