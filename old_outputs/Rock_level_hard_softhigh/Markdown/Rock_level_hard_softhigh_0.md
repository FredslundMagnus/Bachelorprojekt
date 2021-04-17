
# Parameters

    Name :                      Rock_level_hard_softhigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     11.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.05
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      33285783160 function calls (33166610205 primitive calls) in 39315.17 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.166 39315.166 {built-in method builtins.exec}
                      1    0.949    0.949 39315.166 39315.166 <string>:1(<module>)
                      1   92.020   92.020 39314.217 39314.217 main.py:13(teleport)
                2128112    8.587    0.000 13782.694    0.006 game.py:27(step)
                2128112   10.236    0.000 13284.350    0.006 layers.py:373(step)
                4256224   15.291    0.000 11782.286    0.003 agent.py:26(learn)
                4256224  310.776    0.000 10103.595    0.002 learner.py:42(Qlearn)
                2128112  165.509    0.000 9178.138    0.004 layers.py:18(step)
              212811200  443.819    0.000 8994.268    0.000 layer.py:74(move)
                2128112   70.534    0.000 7017.344    0.003 agent.py:50(_learn)
              212811200  649.155    0.000 6966.975    0.000 layers.py:390(check)
                2128112 2889.748    0.001 5229.549    0.002 replaybuffer.py:27(teleporter_save_data)
        134068534/14896590  535.467    0.000 4840.144    0.000 module.py:866(_call_impl)
                2128112   62.866    0.000 4741.406    0.002 agent.py:101(_learn)
               10640366   32.792    0.000 4508.874    0.000 network.py:24(forward)
               10640366  139.884    0.000 4412.095    0.000 container.py:117(forward)
                4256224   35.763    0.000 4246.948    0.001 optimizer.py:84(wrapper)
                2128113  214.195    0.000 4083.093    0.002 layers.py:344(update)
                4256224   17.297    0.000 4076.095    0.001 grad_mode.py:24(decorate_context)
              212811200 3587.278    0.000 4020.757    0.000 layers.py:76(check)
                4256224  117.374    0.000 4020.269    0.001 adam.py:55(step)
                4256224  831.125    0.000 3767.709    0.001 _functional.py:53(adam)
                2128112 2184.660    0.001 3665.159    0.002 agent.py:77(interveen)
                4256030   97.438    0.000 2990.044    0.001 agent.py:45(__call__)
                4256224   18.291    0.000 2491.306    0.001 tensor.py:195(backward)
                4256224   16.073    0.000 2472.374    0.001 __init__.py:68(backward)
                4256224 2363.428    0.001 2363.428    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              161699662 1886.742    0.000 1886.742    0.000 {built-in method clone}
                2128112 1026.493    0.000 1656.572    0.001 agent.py:59(modify)
               19153017 1090.139    0.000 1645.852    0.000 layer.py:119(update)
                5890389   51.376    0.000 1619.826    0.000 layers.py:394(restart)
               21280732   46.579    0.000 1598.451    0.000 conv.py:398(forward)
               21280732   27.213    0.000 1532.876    0.000 conv.py:390(_conv_forward)
               21280732 1505.663    0.000 1505.663    0.000 {built-in method conv2d}
                2128112  745.264    0.000 1480.368    0.001 replaybuffer.py:23(sample_data)
              212811200  303.371    0.000 1390.961    0.000 layers.py:384(isFree)
               27664874   62.147    0.000 1271.062    0.000 linear.py:93(forward)
               27664874   27.131    0.000 1183.003    0.000 functional.py:1737(linear)
               27664874 1150.269    0.000 1150.269    0.000 {built-in method torch._C._nn.linear}
             1545458616  892.517    0.000 1087.590    0.000 layer.py:71(isFree)
                5890389   22.962    0.000 1024.582    0.000 level.py:8(__init__)
                2128112   28.905    0.000  924.244    0.000 agent.py:96(__call__)
                5890389  140.788    0.000  918.017    0.000 levels.py:95(generate)
                6384142   42.689    0.000  913.358    0.000 agent.py:54(modify_board)
             3546825652  583.502    0.000  827.690    0.000 enum.py:646(__hash__)
               76612032  762.866    0.000  762.866    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               19152814  748.212    0.000  748.212    0.000 {built-in method cat}
               38305240   31.367    0.000  709.341    0.000 activation.py:713(forward)
                8813466  697.278    0.000  697.278    0.000 {built-in method tensor}
               76612032  678.840    0.000  678.840    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               38305240   31.389    0.000  677.973    0.000 functional.py:1364(leaky_relu)
               38305240  640.315    0.000  640.315    0.000 {built-in method torch._C._nn.leaky_relu}
                4256224   98.312    0.000  605.824    0.000 optimizer.py:189(zero_grad)
                2128112   38.220    0.000  593.872    0.000 replaybuffer.py:19(stacker)
                6384142  584.152    0.000  584.152    0.000 {built-in method torch._C._nn.one_hot}
                4256224    4.730    0.000  561.056    0.000 game.py:23(board)
              212811200  339.302    0.000  550.824    0.000 layers.py:216(check)
               53013501   74.416    0.000  527.908    0.000 layer.py:48(restart)
              212811300   56.619    0.000  521.681    0.000 {built-in method builtins.all}
              212811200  316.709    0.000  520.240    0.000 layers.py:230(check)
              168083804  518.503    0.000  518.503    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              212811200  315.147    0.000  512.390    0.000 layers.py:244(check)
               11780778   66.490    0.000  505.469    0.000 level.py:41(notUsed)
              650354480  145.951    0.000  488.986    0.000 layers.py:350(<genexpr>)
             4927118648  436.914    0.000  436.914    0.000 layer.py:67(positions)
                2128112  254.922    0.000  422.698    0.000 collector.py:54(collect)
               38306016  421.428    0.000  421.428    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              212811200  269.704    0.000  400.639    0.000 layers.py:63(check)
             1551276402  365.961    0.000  365.961    0.000 layer.py:114(elements)
               38306016  365.627    0.000  365.627    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               38306016  352.277    0.000  352.277    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              757841650  259.669    0.000  351.566    0.000 layer.py:98(add)
               38306016  344.851    0.000  344.851    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              212811300  215.345    0.000  324.702    0.000 layers.py:110(isDone)
                8018501  114.070    0.000  322.050    0.000 random.py:315(sample)
                4256030  114.835    0.000  312.927    0.000 exploration.py:53(softmaxer)
              326521409  141.302    0.000  290.480    0.000 layer.py:94(remove)
                5890489  143.583    0.000  288.090    0.000 layers.py:33(reset)
               38306016  274.643    0.000  274.643    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              294519450  270.618    0.000  270.618    0.000 level.py:32(inverse)
              212811200  169.283    0.000  261.578    0.000 layers.py:203(check)
             3546841315  244.191    0.000  244.191    0.000 {built-in method builtins.hash}
              268142166  182.927    0.000  225.503    0.000 tensor.py:906(grad)
                4256224    7.399    0.000  205.552    0.000 loss.py:527(forward)
                4256224   15.370    0.000  198.153    0.000 functional.py:2898(mse_loss)
        2236885546/2236885544  155.822    0.000  187.857    0.000 {built-in method builtins.len}
               12768672  177.890    0.000  177.890    0.000 {built-in method sum}
              283169664  109.237    0.000  157.384    0.000 random.py:250(_randbelow_with_getrandbits)
             2326664685  153.814    0.000  153.814    0.000 {method 'append' of 'list' objects}
             1545458616  149.630    0.000  149.630    0.000 layer.py:175(isBlocking)
              212811200   69.710    0.000  147.725    0.000 layers.py:99(<listcomp>)
                4256224  129.888    0.000  129.888    0.000 {built-in method torch._C._nn.mse_loss}
               11780778    9.402    0.000  128.581    0.000 level.py:38(elementsIn)
              326521409  123.141    0.000  123.141    0.000 {method 'remove' of 'list' objects}
               21280732   14.346    0.000  121.341    0.000 flatten.py:39(forward)
                4256861  115.696    0.000  115.696    0.000 {built-in method max}
                6384336    8.981    0.000  113.825    0.000 tensor.py:525(__rsub__)
               21280732  106.995    0.000  106.995    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6384336  103.196    0.000  103.196    0.000 {built-in method rsub}
                4256030   98.372    0.000   98.372    0.000 {built-in method multinomial}


Traceback (most recent call last):
  File "main.py", line 111, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9444626: <Rock_level_hard_softhigh_0> in cluster <dcc> Exited

Job <Rock_level_hard_softhigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 02:08:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 02:08:59 2021
Terminated at Sun Mar 21 13:04:26 2021
Results reported at Sun Mar 21 13:04:26 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   39211.07 sec.
    Max Memory :                                 5348 MB
    Average Memory :                             4012.03 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2844.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39356 sec.
    Turnaround time :                            39328 sec.

The output (if any) is above this job summary.

