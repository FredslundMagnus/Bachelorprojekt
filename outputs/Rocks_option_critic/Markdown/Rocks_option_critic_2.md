[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Rocks_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Rocks
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


      30409071141 function calls (29404851944 primitive calls) in 258900.43 seconds

##    Ordered by: cumulative time
   List reduced from 425 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.433 258900.433 {built-in method builtins.exec}
                      1    0.310    0.310 258900.433 258900.433 <string>:1(<module>)
                      1 3904.233 3904.233 258900.123 258900.123 optionCritic.py:195(option_critic_run)
        1326569347/326993257 9919.757    0.000 100484.044    0.000 module.py:866(_call_impl)
               35711900 9552.001    0.000 100206.741    0.003 optionCritic.py:143(actor_loss_fn)
              111064010  733.536    0.000 91580.517    0.001 optionCritic.py:70(get_state)
              111064010 2636.781    0.000 88599.145    0.001 container.py:117(forward)
                1428476   11.168    0.000 78549.589    0.055 tensor.py:195(backward)
                1428476   12.463    0.000 78538.127    0.055 __init__.py:68(backward)
                1428476 78488.734    0.055 78488.734    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              222128020  861.512    0.000 51925.008    0.000 conv.py:398(forward)
              222128020  380.839    0.000 50735.034    0.000 conv.py:390(_conv_forward)
              222128020 50354.195    0.000 50354.195    0.000 {built-in method conv2d}
               35711900 3724.560    0.000 22167.305    0.001 optionCritic.py:91(get_action)
              438057267 1560.773    0.000 20896.863    0.000 linear.py:93(forward)
                1428476   31.182    0.000 20319.564    0.014 optimizer.py:84(wrapper)
                1428476   17.856    0.000 20194.789    0.014 grad_mode.py:24(decorate_context)
                1428476   97.892    0.000 20143.902    0.014 rmsprop.py:56(step)
                1428476  158.266    0.000 19937.222    0.014 _functional.py:203(rmsprop)
              438057267  565.408    0.000 18735.095    0.000 functional.py:1737(linear)
              438057267 18043.176    0.000 18043.176    0.000 {built-in method torch._C._nn.linear}
               19998658 17245.565    0.001 17245.565    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               35711900 1162.110    0.000 12480.189    0.000 optionCritic.py:80(predict_option_termination)
               71423800 1062.270    0.000 8131.118    0.000 distribution.py:34(__init__)
              333192030  445.317    0.000 7712.876    0.000 activation.py:713(forward)
               35711900  585.491    0.000 7276.299    0.000 categorical.py:115(log_prob)
              333192030  427.439    0.000 7267.559    0.000 functional.py:1364(leaky_relu)
              333192030 6747.897    0.000 6747.897    0.000 {built-in method torch._C._nn.leaky_relu}
               35711900  852.963    0.000 6531.660    0.000 categorical.py:49(__init__)
              108436428  468.924    0.000 6204.772    0.000 optionCritic.py:77(get_Q)
                 357119   81.360    0.000 5527.389    0.015 optionCritic.py:116(critic_loss_fn)
               71780919  444.247    0.000 5001.537    0.000 optionCritic.py:88(get_terminations)
               35711900  263.407    0.000 4405.371    0.000 bernoulli.py:34(__init__)
               35711900 2709.768    0.000 4063.173    0.000 constraints.py:398(check)
                1428476    8.757    0.000 3436.685    0.002 game.py:41(step)
                1428476   13.426    0.000 3332.363    0.002 layers.py:718(step)
               35711900  453.648    0.000 3070.665    0.000 distribution.py:240(_validate_sample)
              111064010  154.004    0.000 2198.108    0.000 activation.py:101(forward)
               35711900 1044.562    0.000 2148.360    0.000 categorical.py:123(entropy)
                1428476   65.087    0.000 2148.035    0.002 layers.py:17(step)
               35711900  185.430    0.000 2078.079    0.000 layer.py:98(move)
               35711900 2073.157    0.000 2073.157    0.000 constraints.py:249(check)
              111064010  135.120    0.000 2044.104    0.000 functional.py:1195(relu)
               35711900 1958.424    0.000 1958.424    0.000 constraints.py:364(check)
              111064010 1880.263    0.000 1880.263    0.000 {built-in method relu}
             1342282583 1793.011    0.000 1793.011    0.000 {built-in method torch._C._get_tracing_state}
              107135700  210.081    0.000 1781.766    0.000 utils.py:106(__get__)
              249983300 1749.387    0.000 1749.387    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               35711900  302.844    0.000 1659.133    0.000 bernoulli.py:86(sample)
              107849938  172.260    0.000 1606.159    0.000 tensor.py:525(__rsub__)
             1718973396 1548.550    0.000 1548.701    0.000 module.py:934(__getattr__)
              107135700 1519.289    0.000 1519.289    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              111064010  109.084    0.000 1506.729    0.000 flatten.py:39(forward)
               35711900  175.370    0.000 1480.405    0.000 layers.py:735(check)
               19998658 1436.591    0.000 1436.591    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              107492819 1411.621    0.000 1411.621    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               35711900   72.858    0.000 1409.351    0.000 categorical.py:88(logits)
              107849938 1401.405    0.000 1401.405    0.000 {built-in method rsub}
              111064010 1397.645    0.000 1397.645    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               35711900  361.200    0.000 1389.947    0.000 categorical.py:108(sample)
               35711900   73.035    0.000 1336.492    0.000 utils.py:82(probs_to_logits)
               71423800  378.955    0.000 1201.294    0.000 functional.py:46(broadcast_tensors)
                1428477  139.709    0.000 1165.064    0.001 layers.py:684(update)
               71780919 1133.702    0.000 1133.702    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               35711900  970.143    0.000 1068.603    0.000 layers.py:77(check)
              107135700 1055.256    0.000 1055.256    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               15713236   44.393    0.000  994.873    0.000 tensor.py:575(__iter__)
             5638236175  971.517    0.000  984.190    0.000 {built-in method builtins.len}
               15713236  916.598    0.000  916.598    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5417341398  862.698    0.000  862.698    0.000 {method 'values' of 'collections.OrderedDict' objects}
               35711900  163.514    0.000  837.893    0.000 utils.py:11(broadcast_all)
               35711900  130.502    0.000  815.091    0.000 utils.py:77(clamp_probs)
               35711900  784.251    0.000  784.251    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               71423800  718.354    0.000  718.354    0.000 {built-in method broadcast_tensors}
              108207057  695.958    0.000  695.958    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               35711900  684.589    0.000  684.589    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1428476   72.010    0.000  683.531    0.000 replaybuffer.py:34(save_option_critic)
                 357119  505.197    0.001  655.950    0.002 replaybuffer.py:42(sample_option_critic)
               35711900  655.047    0.000  655.047    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              214985638  617.724    0.000  617.724    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35711900  599.691    0.000  599.691    0.000 {built-in method clamp}
               71423800  574.967    0.000  574.967    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               36298390  558.787    0.000  558.787    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35711900  516.935    0.000  516.935    0.000 {built-in method bernoulli}
               35711900  450.866    0.000  450.866    0.000 {built-in method all}
                8738192  213.678    0.000  450.781    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               35711900  448.366    0.000  448.366    0.000 {built-in method log}
                1428476   84.072    0.000  446.120    0.000 optimizer.py:189(zero_grad)
               35711900  439.984    0.000  439.984    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               19998658  382.089    0.000  382.089    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               19998658  380.258    0.000  380.258    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7142385  236.704    0.000  351.085    0.000 layer.py:151(update)
               19998658  334.453    0.000  334.453    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               35711900  329.810    0.000  329.810    0.000 {built-in method multinomial}
                 586515    9.641    0.000  329.676    0.001 layers.py:740(restart)
              472792416  228.532    0.000  322.437    0.000 {built-in method builtins.isinstance}
               35711900   55.094    0.000  321.554    0.000 layers.py:729(isFree)
                9642217  295.028    0.000  295.028    0.000 {built-in method tensor}
              111064024  291.742    0.000  291.742    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              107135725   77.642    0.000  291.436    0.000 {built-in method builtins.all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601880: <Rocks_option_critic_2> in cluster <dcc> Done

Job <Rocks_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:20 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:23 2021
Terminated at Sun May  2 21:36:25 2021
Results reported at Sun May  2 21:36:25 2021

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

    CPU time :                                   258893.62 sec.
    Max Memory :                                 710 MB
    Average Memory :                             689.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15674.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258961 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

