
# Parameters

    Name :                      Attempt3_Maze_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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


      37621776710 function calls (36404422946 primitive calls) in 258894.49 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.919 258900.919 {built-in method builtins.exec}
                      1    0.334    0.334 258900.918 258900.918 <string>:1(<module>)
                      1 4249.911 4249.911 258900.584 258900.584 optionCritic.py:195(option_critic_run)
               43741550 8712.472    0.000 104741.645    0.002 optionCritic.py:143(actor_loss_fn)
        1615752220/398512363 9881.192    0.000 102863.148    0.000 module.py:866(_call_impl)
              135248873  758.942    0.000 94319.716    0.001 optionCritic.py:70(get_state)
              135248873 2429.183    0.000 91329.601    0.001 container.py:117(forward)
                1749662   11.936    0.000 59151.722    0.034 tensor.py:195(backward)
                1749662   16.437    0.000 59139.533    0.034 __init__.py:68(backward)
                1749662 59083.814    0.034 59083.814    0.034 {method 'run_backward' of 'torch._C._EngineBase' objects}
              270497746  919.511    0.000 56001.415    0.000 conv.py:398(forward)
              270497746  469.374    0.000 54731.130    0.000 conv.py:390(_conv_forward)
              270497746 54261.756    0.000 54261.756    0.000 {built-in method conv2d}
                1749662   37.989    0.000 39617.764    0.023 optimizer.py:84(wrapper)
                1749662   24.922    0.000 39476.200    0.023 grad_mode.py:24(decorate_context)
                1749662  107.004    0.000 39406.583    0.023 rmsprop.py:56(step)
                1749662  138.058    0.000 39170.641    0.022 _functional.py:203(rmsprop)
               24495250 35512.188    0.001 35512.188    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               43741550 3544.829    0.000 21232.460    0.000 optionCritic.py:91(get_action)
              533761236 1601.468    0.000 19836.217    0.000 linear.py:93(forward)
              533761236  660.020    0.000 17635.950    0.000 functional.py:1737(linear)
              533761236 16849.773    0.000 16849.773    0.000 {built-in method torch._C._nn.linear}
               43741550 1197.785    0.000 13240.070    0.000 optionCritic.py:80(predict_option_termination)
               87483100 1184.320    0.000 7764.600    0.000 distribution.py:34(__init__)
              405746619  554.400    0.000 7614.249    0.000 activation.py:713(forward)
               43741550  621.154    0.000 7099.630    0.000 categorical.py:115(log_prob)
              405746619  500.048    0.000 7059.849    0.000 functional.py:1364(leaky_relu)
              405746619 6459.653    0.000 6459.653    0.000 {built-in method torch._C._nn.leaky_relu}
              131863874  446.476    0.000 6066.898    0.000 optionCritic.py:77(get_Q)
               43741550  815.359    0.000 6038.180    0.000 categorical.py:49(__init__)
               43741550  351.325    0.000 4719.982    0.000 bernoulli.py:34(__init__)
               87658066  425.045    0.000 4589.463    0.000 optionCritic.py:88(get_terminations)
               43741550 2459.030    0.000 3639.598    0.000 constraints.py:398(check)
                1749662    9.807    0.000 3208.044    0.002 game.py:42(step)
                1749662   18.872    0.000 3092.517    0.002 layers.py:827(step)
               43741550  522.556    0.000 2819.574    0.000 distribution.py:240(_validate_sample)
               24495250 2484.431    0.000 2484.431    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 174966   32.204    0.000 2053.214    0.012 optionCritic.py:116(critic_loss_fn)
              135248873  184.997    0.000 2048.248    0.000 activation.py:101(forward)
               43741550  963.927    0.000 1976.621    0.000 categorical.py:123(entropy)
               43741550 1917.249    0.000 1917.249    0.000 constraints.py:364(check)
              135248873  159.906    0.000 1863.251    0.000 functional.py:1195(relu)
               43741550  355.061    0.000 1848.786    0.000 bernoulli.py:86(sample)
              131224650  234.345    0.000 1822.548    0.000 utils.py:106(__get__)
               43741550 1763.063    0.000 1763.063    0.000 constraints.py:249(check)
             2094518024 1700.354    0.000 1700.357    0.000 module.py:934(__getattr__)
                1749662   69.884    0.000 1677.277    0.001 layers.py:17(step)
              135248873 1673.881    0.000 1673.881    0.000 {built-in method relu}
               43741550  122.244    0.000 1600.537    0.000 layer.py:106(move)
              306190850 1543.833    0.000 1543.833    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1634998502 1490.648    0.000 1490.648    0.000 {built-in method torch._C._get_tracing_state}
              135248873  133.462    0.000 1458.363    0.000 flatten.py:39(forward)
              131574582  174.018    0.000 1453.188    0.000 tensor.py:525(__rsub__)
               43741550   77.484    0.000 1407.471    0.000 categorical.py:88(logits)
               43741550  377.986    0.000 1392.630    0.000 categorical.py:108(sample)
                1749663  160.490    0.000 1388.340    0.001 layers.py:793(update)
               87483100  482.101    0.000 1354.876    0.000 functional.py:46(broadcast_tensors)
               43741550   76.542    0.000 1329.987    0.000 utils.py:82(probs_to_logits)
              135248873 1324.900    0.000 1324.900    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              131224650 1311.207    0.000 1311.207    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              131574582 1252.212    0.000 1252.212    0.000 {built-in method rsub}
              131399616 1245.462    0.000 1245.462    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               87658066 1128.107    0.000 1128.107    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             7021168252 1083.480    0.000 1098.887    0.000 {built-in method builtins.len}
               19246282   49.522    0.000 1081.779    0.000 tensor.py:575(__iter__)
               43741550  200.500    0.000 1012.436    0.000 utils.py:11(broadcast_all)
               19246282 1000.818    0.000 1000.818    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               43741550  252.733    0.000  976.791    0.000 layers.py:844(check)
             6598257753  953.573    0.000  953.573    0.000 {method 'values' of 'collections.OrderedDict' objects}
              131224650  922.486    0.000  922.486    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               43741550  149.801    0.000  829.964    0.000 utils.py:77(clamp_probs)
               43741550  818.097    0.000  818.097    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               87483100  755.128    0.000  755.128    0.000 {built-in method broadcast_tensors}
               43741550  680.163    0.000  680.163    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1749662   77.507    0.000  647.843    0.000 replaybuffer.py:34(save_option_critic)
               43741550  642.335    0.000  642.335    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              131749548  607.480    0.000  607.480    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               44030842  553.712    0.000  553.712    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              262799232  552.051    0.000  552.051    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               43741550  550.648    0.000  550.648    0.000 {built-in method clamp}
               87483100  543.801    0.000  543.801    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               43741550  528.597    0.000  528.597    0.000 {built-in method bernoulli}
                1749662   88.775    0.000  513.610    0.000 optimizer.py:189(zero_grad)
               13997304  255.321    0.000  428.038    0.000 layer.py:175(NoRock_update)
               43741550  423.481    0.000  423.481    0.000 {built-in method log}
               43741550   85.726    0.000  423.458    0.000 layers.py:838(isFree)
               24495250  411.282    0.000  411.282    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               43741550  410.962    0.000  410.962    0.000 {built-in method all}
               43741550  400.994    0.000  400.994    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                 174966  286.331    0.002  358.243    0.002 replaybuffer.py:42(sample_option_critic)
                 289316    7.459    0.000  345.736    0.001 layers.py:849(restart)
              231904000  285.807    0.000  337.732    0.000 layer.py:103(isFree)
              578167952  228.412    0.000  334.357    0.000 {built-in method builtins.isinstance}
               43741550  328.912    0.000  328.912    0.000 {built-in method multinomial}
               24495250  323.246    0.000  323.246    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11022874  318.461    0.000  318.461    0.000 {built-in method tensor}
              131517464  312.419    0.000  312.419    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              131224675   91.019    0.000  302.426    0.000 {built-in method builtins.all}
               24495250  301.436    0.000  301.436    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              135248887  298.558    0.000  298.558    0.000 {method 'to' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 239, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607863: <Attempt3_Maze_option_critic_2> in cluster <dcc> Exited

Job <Attempt3_Maze_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:26 2021
Job was executed on host(s) <n-62-21-97>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:28 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258926.58 sec.
    Max Memory :                                 895 MB
    Average Memory :                             887.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15489.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258926 sec.
    Turnaround time :                            258907 sec.

The output (if any) is above this job summary.

