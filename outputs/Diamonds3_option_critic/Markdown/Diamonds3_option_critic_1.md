
# Parameters

    Name :                      Diamonds3_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      54081464814 function calls (52365892158 primitive calls) in 258900.47 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.471 258900.471 {built-in method builtins.exec}
                      1    0.371    0.371 258900.470 258900.470 <string>:1(<module>)
                      1 6309.250 6309.250 258900.099 258900.099 optionCritic.py:195(option_critic_run)
               61008975 9473.240    0.000 112751.489    0.002 optionCritic.py:143(actor_loss_fn)
        2265740905/558099706 10023.380    0.000 112293.459    0.000 module.py:866(_call_impl)
              189737911  865.438    0.000 104647.019    0.001 optionCritic.py:70(get_state)
              189737911 2272.831    0.000 101201.468    0.001 container.py:117(forward)
                2440359   19.897    0.000 72301.246    0.030 tensor.py:195(backward)
                2440359   26.180    0.000 72281.014    0.030 __init__.py:68(backward)
                2440359 72198.274    0.030 72198.274    0.030 {method 'run_backward' of 'torch._C._EngineBase' objects}
              379475822  935.104    0.000 63752.894    0.000 conv.py:398(forward)
              379475822  513.144    0.000 62416.974    0.000 conv.py:390(_conv_forward)
              379475822 61903.831    0.000 61903.831    0.000 {built-in method conv2d}
               61008975 3716.885    0.000 21672.561    0.000 optionCritic.py:91(get_action)
              747837617 1618.211    0.000 21510.081    0.000 linear.py:93(forward)
              747837617  644.260    0.000 19206.867    0.000 functional.py:1737(linear)
              747837617 18402.400    0.000 18402.400    0.000 {built-in method torch._C._nn.linear}
               61008975 1270.574    0.000 14589.427    0.000 optionCritic.py:80(predict_option_termination)
              122017950 1326.270    0.000 8311.924    0.000 distribution.py:34(__init__)
                2440359   58.582    0.000 7801.234    0.003 optimizer.py:84(wrapper)
                2440359   30.738    0.000 7590.998    0.003 grad_mode.py:24(decorate_context)
                2440359  139.000    0.000 7506.448    0.003 rmsprop.py:56(step)
              569213733  519.673    0.000 7459.416    0.000 activation.py:713(forward)
                2440359  137.388    0.000 7211.863    0.003 _functional.py:203(rmsprop)
               61008975  598.619    0.000 7152.919    0.000 categorical.py:115(log_prob)
              569213733  560.634    0.000 6939.744    0.000 functional.py:1364(leaky_relu)
              569213733 6270.026    0.000 6270.026    0.000 {built-in method torch._C._nn.leaky_relu}
               61008975  823.992    0.000 6092.550    0.000 categorical.py:49(__init__)
               61008975  504.190    0.000 5784.499    0.000 bernoulli.py:34(__init__)
              184724781  381.970    0.000 5680.769    0.000 optionCritic.py:77(get_Q)
                 610089   99.915    0.000 5025.292    0.008 optionCritic.py:116(critic_loss_fn)
              122628039  409.992    0.000 4451.016    0.000 optionCritic.py:88(get_terminations)
                2440359   12.042    0.000 4097.216    0.002 game.py:41(step)
                2440359   22.757    0.000 3945.819    0.002 layers.py:718(step)
               61008975 2494.695    0.000 3695.504    0.000 constraints.py:398(check)
               34165020 3334.242    0.000 3334.242    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               61008975  517.646    0.000 2914.117    0.000 distribution.py:240(_validate_sample)
               34165020 2370.919    0.000 2370.919    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2440359   91.620    0.000 2311.565    0.001 layers.py:17(step)
               61008975  156.854    0.000 2212.194    0.000 layer.py:98(move)
               61008975  454.638    0.000 2172.940    0.000 bernoulli.py:86(sample)
              189737911  242.724    0.000 2129.291    0.000 activation.py:101(forward)
               61008975 2097.022    0.000 2097.022    0.000 constraints.py:364(check)
               61008975 1039.955    0.000 1986.877    0.000 categorical.py:123(entropy)
              189737911  202.312    0.000 1886.567    0.000 functional.py:1195(relu)
               61008975 1877.616    0.000 1877.616    0.000 constraints.py:249(check)
             2935061833 1850.402    0.000 1850.581    0.000 module.py:934(__getattr__)
              427062825 1805.559    0.000 1805.559    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              183026925  250.008    0.000 1796.140    0.000 utils.py:106(__get__)
              189737911 1654.752    0.000 1654.752    0.000 {built-in method relu}
              189737911  177.934    0.000 1648.307    0.000 flatten.py:39(forward)
                2440360  210.126    0.000 1602.521    0.001 layers.py:684(update)
              184247103  205.959    0.000 1598.640    0.000 tensor.py:525(__rsub__)
              122017950  551.141    0.000 1569.751    0.000 functional.py:46(broadcast_tensors)
                 610089 1298.285    0.002 1549.918    0.003 replaybuffer.py:42(sample_option_critic)
               26843949   61.685    0.000 1480.563    0.000 tensor.py:575(__iter__)
              189737911 1470.372    0.000 1470.372    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               61008975  291.479    0.000 1440.978    0.000 layers.py:735(check)
               61008975  397.187    0.000 1427.655    0.000 categorical.py:108(sample)
               26843949 1382.004    0.000 1382.004    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              184247103 1362.075    0.000 1362.075    0.000 {built-in method rsub}
               61008975   70.745    0.000 1361.662    0.000 categorical.py:88(logits)
               61008975  291.788    0.000 1328.280    0.000 utils.py:11(broadcast_all)
               61008975   80.338    0.000 1290.917    0.000 utils.py:82(probs_to_logits)
              122628039 1274.289    0.000 1274.289    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             2292584854 1264.432    0.000 1264.432    0.000 {built-in method torch._C._get_tracing_state}
              183026925 1252.582    0.000 1252.582    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              183637014 1247.161    0.000 1247.161    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9863975775 1158.293    0.000 1177.406    0.000 {built-in method builtins.len}
              183026925 1029.085    0.000 1029.085    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9252701531  961.744    0.000  961.744    0.000 {method 'values' of 'collections.OrderedDict' objects}
               61008975  947.218    0.000  947.218    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              122017950  847.612    0.000  847.612    0.000 {built-in method broadcast_tensors}
                2440359   89.701    0.000  796.766    0.000 replaybuffer.py:34(save_option_critic)
                2440359  111.056    0.000  779.337    0.000 optimizer.py:189(zero_grad)
               61008975  162.166    0.000  759.335    0.000 utils.py:77(clamp_probs)
              184857192  669.844    0.000  669.844    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               61008975  655.628    0.000  655.628    0.000 {built-in method bernoulli}
               61008975  603.780    0.000  603.780    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               61008975  597.170    0.000  597.170    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               61486653  576.290    0.000  576.290    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               34165020  574.079    0.000  574.079    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              122017950  534.521    0.000  534.521    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              367274028  533.095    0.000  533.095    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11919723  248.368    0.000  531.160    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               34165020  512.027    0.000  512.027    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               19522880  305.871    0.000  508.551    0.000 layer.py:167(NoRock_update)
               61008975  508.111    0.000  508.111    0.000 {built-in method clamp}
               61008975  100.914    0.000  498.029    0.000 layers.py:729(isFree)
               16472425  487.925    0.000  487.925    0.000 {built-in method tensor}
               61008975  451.243    0.000  451.243    0.000 {built-in method log}
              805697739  296.772    0.000  445.996    0.000 {built-in method builtins.isinstance}
              183026950  126.642    0.000  443.268    0.000 {built-in method builtins.all}
               61008975  431.011    0.000  431.011    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              183509507  413.411    0.000  413.411    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              189737925  405.680    0.000  405.680    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               61008975  401.880    0.000  401.880    0.000 {built-in method all}
              336612222  334.424    0.000  397.115    0.000 layer.py:95(isFree)
               34165006  393.025    0.000  393.025    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7321081   16.163    0.000  380.608    0.000 game.py:37(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601864: <Diamonds3_option_critic_1> in cluster <dcc> Done

Job <Diamonds3_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:09 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:12 2021
Terminated at Sun May  2 21:36:14 2021
Results reported at Sun May  2 21:36:14 2021

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

    CPU time :                                   258285.97 sec.
    Max Memory :                                 906 MB
    Average Memory :                             888.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15478.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258916 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

