[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      31063600106 function calls (30152717637 primitive calls) in 258900.71 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.708 258900.708 {built-in method builtins.exec}
                      1    0.330    0.330 258900.708 258900.708 <string>:1(<module>)
                      1 3370.153 3370.153 258900.378 258900.378 optionCritic.py:195(option_critic_run)
        1202949027/296278065 8727.835    0.000 112606.318    0.000 module.py:866(_call_impl)
               32392675 8692.806    0.000 105701.544    0.003 optionCritic.py:143(actor_loss_fn)
              100741218  656.771    0.000 104667.839    0.001 optionCritic.py:70(get_state)
              100741218 2437.966    0.000 102010.901    0.001 container.py:117(forward)
                1295707   10.186    0.000 86746.452    0.067 tensor.py:195(backward)
                1295707   11.814    0.000 86736.028    0.067 __init__.py:68(backward)
                1295707 86690.896    0.067 86690.896    0.067 {method 'run_backward' of 'torch._C._EngineBase' objects}
              201482436  779.341    0.000 68819.757    0.000 conv.py:398(forward)
              201482436  312.697    0.000 67748.879    0.000 conv.py:390(_conv_forward)
              201482436 67436.182    0.000 67436.182    0.000 {built-in method conv2d}
               32392675 3406.761    0.000 20054.038    0.001 optionCritic.py:91(get_action)
              397019283 1382.669    0.000 19029.637    0.000 linear.py:93(forward)
              397019283  492.378    0.000 17111.919    0.000 functional.py:1737(linear)
              397019283 16506.232    0.000 16506.232    0.000 {built-in method torch._C._nn.linear}
               32392675 1041.819    0.000 11289.997    0.000 optionCritic.py:80(predict_option_termination)
                 323926   74.696    0.000 7798.651    0.024 optionCritic.py:116(critic_loss_fn)
               64785350  933.423    0.000 7377.928    0.000 distribution.py:34(__init__)
              302223654  377.750    0.000 6997.989    0.000 activation.py:713(forward)
              302223654  366.709    0.000 6620.239    0.000 functional.py:1364(leaky_relu)
               32392675  523.246    0.000 6529.482    0.000 categorical.py:115(log_prob)
              302223654 6173.209    0.000 6173.209    0.000 {built-in method torch._C._nn.leaky_relu}
               32392675  774.600    0.000 5933.479    0.000 categorical.py:49(__init__)
               98034896  402.732    0.000 5519.966    0.000 optionCritic.py:77(get_Q)
               65109276  390.078    0.000 4477.539    0.000 optionCritic.py:88(get_terminations)
                1295707   27.192    0.000 4185.344    0.003 optimizer.py:84(wrapper)
                1295707    7.931    0.000 4153.348    0.003 game.py:41(step)
                1295707   13.639    0.000 4076.287    0.003 grad_mode.py:24(decorate_context)
                1295707   12.296    0.000 4042.306    0.003 layers.py:718(step)
                1295707   90.080    0.000 4035.026    0.003 rmsprop.py:56(step)
               32392675  254.199    0.000 4023.533    0.000 bernoulli.py:34(__init__)
                1295707  136.713    0.000 3844.871    0.003 _functional.py:203(rmsprop)
               32392675 2456.084    0.000 3692.467    0.000 constraints.py:398(check)
                1295707   59.139    0.000 2809.020    0.002 layers.py:17(step)
               32392675  404.656    0.000 2765.191    0.000 distribution.py:240(_validate_sample)
               32392675  200.250    0.000 2745.366    0.000 layer.py:98(move)
               18139892 1992.916    0.000 1992.916    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              100741218  143.517    0.000 1974.970    0.000 activation.py:101(forward)
               32392675  948.326    0.000 1941.913    0.000 categorical.py:123(entropy)
               32392675  302.753    0.000 1901.555    0.000 layers.py:735(check)
               32392675 1873.629    0.000 1873.629    0.000 constraints.py:249(check)
              100741218  127.604    0.000 1831.453    0.000 functional.py:1195(relu)
               32392675 1781.022    0.000 1781.022    0.000 constraints.py:364(check)
              100741218 1679.113    0.000 1679.113    0.000 {built-in method relu}
              226748725 1653.196    0.000 1653.196    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               97178025  188.881    0.000 1606.640    0.000 utils.py:106(__get__)
             1217201804 1531.267    0.000 1531.267    0.000 {built-in method torch._C._get_tracing_state}
               32392675  286.494    0.000 1524.480    0.000 bernoulli.py:86(sample)
               97825877  167.525    0.000 1465.583    0.000 tensor.py:525(__rsub__)
              100741218  106.336    0.000 1388.543    0.000 flatten.py:39(forward)
             1558235354 1382.504    0.000 1382.634    0.000 module.py:934(__getattr__)
               97178025 1368.173    0.000 1368.173    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              100741218 1282.207    0.000 1282.207    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               32392675   63.152    0.000 1276.764    0.000 categorical.py:88(logits)
               97825877 1270.317    0.000 1270.317    0.000 {built-in method rsub}
               97501951 1268.806    0.000 1268.806    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               32392675  321.668    0.000 1247.796    0.000 categorical.py:108(sample)
                1295708  126.239    0.000 1215.688    0.001 layers.py:684(update)
               32392675   68.262    0.000 1213.613    0.000 utils.py:82(probs_to_logits)
               64785350  348.929    0.000 1080.706    0.000 functional.py:46(broadcast_tensors)
               65109276 1042.869    0.000 1042.869    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               97178025  944.631    0.000  944.631    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               14252777   39.539    0.000  933.307    0.000 tensor.py:575(__iter__)
             5338539433  895.845    0.000  907.160    0.000 {built-in method builtins.len}
               14252777  863.596    0.000  863.596    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               32392675  160.598    0.000  779.340    0.000 utils.py:11(broadcast_all)
             4912537326  768.007    0.000  768.007    0.000 {method 'values' of 'collections.OrderedDict' objects}
               32392675  114.500    0.000  738.514    0.000 utils.py:77(clamp_probs)
               13328057  342.753    0.000  726.168    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               32392675  713.434    0.000  713.434    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               64785350  637.870    0.000  637.870    0.000 {built-in method broadcast_tensors}
                1295707   65.305    0.000  624.778    0.000 replaybuffer.py:34(save_option_critic)
               32392675  624.014    0.000  624.014    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               98149803  616.480    0.000  616.480    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                 323926  454.892    0.001  600.605    0.002 replaybuffer.py:42(sample_option_critic)
               32392675  583.228    0.000  583.228    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              195003902  547.943    0.000  547.943    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               32392675  544.341    0.000  544.341    0.000 {built-in method clamp}
               18139892  522.514    0.000  522.514    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               32392675  116.691    0.000  520.863    0.000 layers.py:729(isFree)
               64785350  518.016    0.000  518.016    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               32601694  498.682    0.000  498.682    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               32392675  470.742    0.000  470.742    0.000 {built-in method bernoulli}
               14252788  287.068    0.000  457.875    0.000 layer.py:151(update)
               18139892  452.037    0.000  452.037    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1295707   78.943    0.000  430.351    0.000 optimizer.py:189(zero_grad)
               32392675  322.578    0.000  428.926    0.000 layers.py:471(check)
               32392675  414.169    0.000  414.169    0.000 {built-in method all}
               18139892  408.643    0.000  408.643    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               32392675  406.837    0.000  406.837    0.000 {built-in method log}
              323016333  328.153    0.000  404.172    0.000 layer.py:95(isFree)
               32392675  401.123    0.000  401.123    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               97178050   91.141    0.000  387.850    0.000 {built-in method builtins.all}
               13328057   21.632    0.000  383.416    0.000 <__array_function__ internals>:2(prod)
               13328057   21.011    0.000  357.502    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               13328057   39.150    0.000  336.491    0.000 fromnumeric.py:2912(prod)
              887439922  230.450    0.000  333.083    0.000 enum.py:646(__hash__)
               18139892  332.048    0.000  332.048    0.000 {method 'add_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601872: <SuperLevel2_option_critic_0> in cluster <dcc> Done

Job <SuperLevel2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:15 2021
Job was executed on host(s) <n-62-23-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:17 2021
Terminated at Sun May  2 21:36:23 2021
Results reported at Sun May  2 21:36:23 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258861.36 sec.
    Max Memory :                                 1184 MB
    Average Memory :                             1154.90 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15200.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

