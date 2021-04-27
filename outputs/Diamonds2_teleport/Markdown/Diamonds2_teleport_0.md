
# Parameters

    Name :                      Diamonds2_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      73674790139 function calls (73465339504 primitive calls) in 86106.16 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86106.162 86106.162 {built-in method builtins.exec}
                      1    1.563    1.563 86106.162 86106.162 <string>:1(<module>)
                      1  176.731  176.731 86104.600 86104.600 main.py:45(teleport)
                7480924   27.075    0.000 28104.185    0.004 agent.py:29(learn)
                7480924  651.534    0.000 24111.415    0.003 learner.py:42(Qlearn)
                3740462   16.515    0.000 21564.656    0.006 game.py:41(step)
                3740462   21.938    0.000 20601.910    0.006 layers.py:718(step)
                3740462  129.978    0.000 16881.612    0.005 agent.py:54(_learn)
                3740462 6925.279    0.002 13370.578    0.004 replaybuffer.py:28(teleporter_save_data)
                3740462  311.732    0.000 12212.241    0.003 layers.py:17(step)
              374046200  658.044    0.000 11867.085    0.000 layer.py:98(move)
                3740462  109.090    0.000 11179.439    0.003 agent.py:117(_learn)
        235631504/26181880  987.840    0.000 10880.057    0.000 module.py:715(_call_impl)
                7480924   46.449    0.000 10369.640    0.001 grad_mode.py:23(decorate_context)
                7480924  259.173    0.000 10233.437    0.001 adam.py:55(step)
               18700956   52.523    0.000 10199.347    0.001 network.py:27(forward)
                3740462 6774.674    0.002 10094.342    0.003 agent.py:88(interveen)
               18700956  255.990    0.000 10029.859    0.001 container.py:115(forward)
                7480924 1878.227    0.000 8793.364    0.001 functional.py:53(adam)
                3740463  555.912    0.000 8342.255    0.002 layers.py:684(update)
              374046200 1553.955    0.000 7826.571    0.000 layers.py:735(check)
                7479570  178.548    0.000 6675.521    0.001 agent.py:49(__call__)
                7480924   46.346    0.000 5469.004    0.001 tensor.py:181(backward)
                7480924   27.678    0.000 5422.658    0.001 __init__.py:68(backward)
                7480924 5185.648    0.001 5185.648    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              325855034 5040.569    0.000 5040.569    0.000 {built-in method clone}
                3740462 2881.591    0.001 4725.117    0.001 replaybuffer.py:22(sample_data)
                3740462 2399.968    0.001 4502.487    0.001 agent.py:67(modify)
               37401912   67.578    0.000 3637.766    0.000 conv.py:422(forward)
               37401912   78.179    0.000 3544.434    0.000 conv.py:414(_conv_forward)
               37401912 3452.570    0.000 3452.570    0.000 {built-in method conv2d}
               48621944  116.563    0.000 3260.919    0.000 linear.py:92(forward)
               48621944  198.524    0.000 3093.593    0.000 functional.py:1669(linear)
                5373660   57.732    0.000 2845.036    0.001 layers.py:740(restart)
              374046200  749.692    0.000 2761.895    0.000 layers.py:729(isFree)
                5373660   28.273    0.000 2361.319    0.000 level.py:8(__init__)
             1045689586  643.917    0.000 2256.216    0.000 {built-in method builtins.any}
              471298266 1428.253    0.000 2237.143    0.000 tensor.py:933(grad)
               48621944 2226.518    0.000 2226.518    0.000 {built-in method addmm}
               33664167 1254.878    0.000 2213.674    0.000 layer.py:167(NoRock_update)
                7480924  190.940    0.000 2124.478    0.000 optimizer.py:167(zero_grad)
                3740462   52.005    0.000 2102.165    0.001 agent.py:112(__call__)
                5373660   86.277    0.000 2085.435    0.000 levels.py:249(generate)
             3299630710 1569.488    0.000 2012.204    0.000 layer.py:95(isFree)
             7297720385 1381.280    0.000 2000.908    0.000 enum.py:646(__hash__)
               11220032   86.137    0.000 1986.624    0.000 agent.py:59(modify_board)
               29922342 1932.436    0.000 1932.436    0.000 {built-in method cat}
               34927469  347.114    0.000 1907.971    0.000 level.py:41(notUsed)
              134656632 1835.259    0.000 1835.259    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3740462   68.019    0.000 1557.166    0.000 replaybuffer.py:18(stacker)
              134656632 1555.879    0.000 1555.879    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              337075066 1525.430    0.000 1525.430    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               67322900   58.955    0.000 1507.427    0.000 activation.py:713(forward)
               67322900   90.231    0.000 1448.472    0.000 functional.py:1292(leaky_relu)
               67322900 1349.265    0.000 1349.265    0.000 {built-in method torch._C._nn.leaky_relu}
               16044183 1347.392    0.000 1347.392    0.000 {built-in method tensor}
               11220032 1242.250    0.000 1242.250    0.000 {built-in method torch._C._nn.one_hot}
             3686726400  995.496    0.000 1224.387    0.000 layers.py:700(<genexpr>)
              374046200  726.217    0.000 1192.755    0.000 layers.py:349(check)
              374046200  679.181    0.000 1099.697    0.000 layers.py:387(check)
              374046200  676.242    0.000 1090.108    0.000 layers.py:375(check)
               26185284  147.583    0.000 1078.945    0.000 tensor.py:21(wrapped)
              374046200  653.291    0.000 1068.123    0.000 layers.py:337(check)
              613433153  354.223    0.000 1044.677    0.000 overrides.py:1070(has_torch_function)
                7480924    9.265    0.000 1027.698    0.000 game.py:37(board)
               67328316 1007.520    0.000 1007.520    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              400231584  169.372    0.000 1005.910    0.000 {built-in method builtins.all}
                3740462  577.980    0.000  969.914    0.000 collector.py:46(collect)
               67328316  918.126    0.000  918.126    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               34927469   27.105    0.000  882.729    0.000 level.py:38(elementsIn)
             8635456286  881.297    0.000  881.297    0.000 layer.py:91(positions)
             1554881544  433.561    0.000  866.671    0.000 layers.py:690(<genexpr>)
               67328316  831.371    0.000  831.371    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67328316  744.300    0.000  744.300    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7479570  255.321    0.000  719.941    0.000 exploration.py:53(softmaxer)
             7297747712  619.632    0.000  619.632    0.000 {built-in method builtins.hash}
               67328316  586.003    0.000  586.003    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               34927469  277.875    0.000  566.128    0.000 level.py:39(<listcomp>)
             1197170703  562.162    0.000  562.162    0.000 layer.py:146(elements)
              374046200  346.494    0.000  537.443    0.000 layers.py:364(check)
              374046200  322.592    0.000  504.376    0.000 layers.py:326(check)
        4681568324/4681568322  359.097    0.000  476.347    0.000 {built-in method builtins.len}
                7480924   11.240    0.000  455.544    0.000 loss.py:445(forward)
               18702310  454.192    0.000  454.192    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7480924   41.637    0.000  444.305    0.000 functional.py:2637(mse_loss)
               48621944  436.852    0.000  436.852    0.000 {method 't' of 'torch._C._TensorBase' objects}
              374046200  286.500    0.000  426.364    0.000 layers.py:23(check)
             1647302717  412.825    0.000  412.825    0.000 level.py:32(inverse)
               48362940   41.377    0.000  409.065    0.000 layer.py:69(restart)
               22442772  390.412    0.000  390.412    0.000 {built-in method sum}
             1301672787  304.424    0.000  382.585    0.000 overrides.py:1083(<genexpr>)
             3299630710  364.172    0.000  364.172    0.000 layer.py:203(isBlocking)
              567576971  243.432    0.000  334.371    0.000 layer.py:130(add)
             3776444422  326.985    0.000  326.985    0.000 {method 'random' of '_random.Random' objects}
                5373760  149.889    0.000  297.549    0.000 layers.py:36(reset)
              381517465  196.508    0.000  291.368    0.000 layer.py:126(remove)
               34927469  179.338    0.000  289.495    0.000 {built-in method _functools.reduce}
                7480924  283.213    0.000  283.213    0.000 {built-in method torch._C._nn.mse_loss}
                3740462  102.437    0.000  279.493    0.000 random.py:315(sample)
             1450842206  278.053    0.000  278.053    0.000 enum.py:352(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550899: <Diamonds2_teleport_0> in cluster <dcc> Done

Job <Diamonds2_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 07:27:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 07:27:55 2021
Terminated at Fri Apr 23 07:23:04 2021
Results reported at Fri Apr 23 07:23:04 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85897.91 sec.
    Max Memory :                                 2679 MB
    Average Memory :                             2676.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13705.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            226876 sec.

The output (if any) is above this job summary.

