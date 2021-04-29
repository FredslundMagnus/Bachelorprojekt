
# Parameters

    Name :                      Coconuts_teleport-0
    Main :                      teleport
    Level :                     Levels.Coconuts
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


      92500427637 function calls (92188286914 primitive calls) in 86114.00 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.001 86114.001 {built-in method builtins.exec}
                      1    1.510    1.510 86114.001 86114.001 <string>:1(<module>)
                      1  230.906  230.906 86112.491 86112.491 main.py:45(teleport)
               11178338   37.201    0.000 30298.216    0.003 agent.py:29(learn)
                5589169   21.715    0.000 28667.672    0.005 game.py:41(step)
                5589169   27.108    0.000 27520.566    0.005 layers.py:718(step)
               11178338  717.581    0.000 25537.591    0.002 learner.py:42(Qlearn)
                5589169  460.674    0.000 19050.588    0.003 layers.py:17(step)
              558916900 1947.179    0.000 18542.728    0.000 layer.py:98(move)
                5589169  179.881    0.000 18297.669    0.003 agent.py:54(_learn)
        351192749/39053037 1237.258    0.000 12382.463    0.000 module.py:715(_call_impl)
                5589169  148.012    0.000 11940.948    0.002 agent.py:117(_learn)
              558916900 2005.008    0.000 11570.317    0.000 layers.py:735(check)
               27874699   65.817    0.000 11558.518    0.000 network.py:27(forward)
               27874699  294.462    0.000 11340.333    0.000 container.py:115(forward)
               11178338   67.015    0.000 10191.153    0.001 grad_mode.py:23(decorate_context)
               11178338  335.634    0.000 10005.857    0.001 adam.py:55(step)
                5589170  734.925    0.000 8404.417    0.002 layers.py:684(update)
               11178338 1851.175    0.000 8237.837    0.001 functional.py:53(adam)
               11107192  228.914    0.000 7622.336    0.001 agent.py:49(__call__)
                5589169 4215.737    0.001 6559.824    0.001 replaybuffer.py:22(sample_data)
                5589169 2685.722    0.000 6429.465    0.001 agent.py:88(interveen)
               11178338   71.095    0.000 6195.299    0.001 tensor.py:181(backward)
               11178338   37.358    0.000 6124.204    0.001 __init__.py:68(backward)
               11178338 5844.948    0.001 5844.948    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5589169 2787.406    0.000 5109.944    0.001 replaybuffer.py:28(teleporter_save_data)
                5589169 2471.648    0.000 4839.626    0.001 agent.py:67(modify)
               55749398   87.672    0.000 4199.830    0.000 conv.py:422(forward)
               55749398  103.046    0.000 4075.950    0.000 conv.py:414(_conv_forward)
               55749398 3952.226    0.000 3952.226    0.000 {built-in method conv2d}
              558916900  776.984    0.000 3703.541    0.000 layers.py:729(isFree)
               72445759  152.419    0.000 3678.761    0.000 linear.py:92(forward)
              558916900 2560.850    0.000 3601.885    0.000 layers.py:471(check)
               72445759  254.673    0.000 3453.776    0.000 functional.py:1669(linear)
              558916900 2106.160    0.000 2931.329    0.000 layers.py:77(check)
             3669428170 2381.226    0.000 2926.557    0.000 layer.py:95(isFree)
               39124190 1766.675    0.000 2856.909    0.000 layer.py:151(update)
             1566847599  782.634    0.000 2634.405    0.000 {built-in method builtins.any}
              704235348 1554.023    0.000 2566.934    0.000 tensor.py:933(grad)
               72445759 2447.632    0.000 2447.632    0.000 {built-in method addmm}
                5589169   66.591    0.000 2417.918    0.000 agent.py:112(__call__)
               44642206 2357.511    0.000 2357.511    0.000 {built-in method cat}
               16696361  104.556    0.000 2307.747    0.000 agent.py:59(modify_board)
                3285079   34.667    0.000 2304.569    0.001 layers.py:740(restart)
             9082323624 1560.718    0.000 2262.038    0.000 enum.py:646(__hash__)
               11178338  203.757    0.000 2210.714    0.000 optimizer.py:167(zero_grad)
                5589169   88.562    0.000 1959.134    0.000 replaybuffer.py:18(stacker)
                3285079   17.386    0.000 1947.856    0.001 level.py:8(__init__)
              185701248 1909.067    0.000 1909.067    0.000 {built-in method clone}
                3285079  125.931    0.000 1750.838    0.001 levels.py:262(generate)
              201210084 1629.319    0.000 1629.319    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               23814713 1595.222    0.000 1595.222    0.000 {built-in method tensor}
              100320458   79.017    0.000 1578.282    0.000 activation.py:713(forward)
               29297352  258.955    0.000 1514.603    0.000 level.py:41(notUsed)
              100320458  123.137    0.000 1499.265    0.000 functional.py:1292(leaky_relu)
               16696361 1485.860    0.000 1485.860    0.000 {built-in method torch._C._nn.one_hot}
              916413242  464.410    0.000 1382.194    0.000 overrides.py:1070(has_torch_function)
              100320458 1364.358    0.000 1364.358    0.000 {built-in method torch._C._nn.leaky_relu}
              201210084 1354.905    0.000 1354.905    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              558916900 1008.038    0.000 1340.132    0.000 layers.py:62(check)
             4445055368 1091.838    0.000 1338.066    0.000 layers.py:700(<genexpr>)
               39128113  195.211    0.000 1319.158    0.000 tensor.py:21(wrapped)
               11178338   13.267    0.000 1250.098    0.000 game.py:37(board)
            11963999042 1057.925    0.000 1057.925    0.000 layer.py:91(positions)
              100605042 1018.050    0.000 1018.050    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5589169  553.995    0.000  955.563    0.000 collector.py:46(collect)
              100605042  890.636    0.000  890.636    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11107192  296.275    0.000  794.673    0.000 exploration.py:53(softmaxer)
              100605042  784.625    0.000  784.625    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              558916900  460.239    0.000  701.536    0.000 layers.py:48(check)
             9082364199  701.327    0.000  701.327    0.000 {built-in method builtins.hash}
              100605042  682.647    0.000  682.647    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               29297352   27.499    0.000  678.001    0.000 level.py:38(elementsIn)
             1605960184  670.264    0.000  670.264    0.000 layer.py:146(elements)
              598045113  122.348    0.000  584.855    0.000 {built-in method builtins.all}
              558916900  396.075    0.000  583.717    0.000 layers.py:23(check)
              202397609  579.855    0.000  579.855    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        5578760632/5578760630  389.888    0.000  537.120    0.000 {built-in method builtins.len}
               11178338   14.904    0.000  535.258    0.000 loss.py:445(forward)
               11178338   58.951    0.000  520.354    0.000 functional.py:2637(mse_loss)
              100605042  510.973    0.000  510.973    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1944399246  410.997    0.000  506.540    0.000 overrides.py:1083(<genexpr>)
             1191407318  248.516    0.000  501.206    0.000 layers.py:690(<genexpr>)
               27945845  483.958    0.000  483.958    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              569940722  289.301    0.000  454.849    0.000 layer.py:126(remove)
               72445759  447.348    0.000  447.348    0.000 {method 't' of 'torch._C._TensorBase' objects}
               29297352  215.170    0.000  435.903    0.000 level.py:39(<listcomp>)
              764690175  300.827    0.000  406.050    0.000 layer.py:130(add)
               33535014  387.907    0.000  387.907    0.000 {built-in method sum}
                5589169  140.564    0.000  375.105    0.000 random.py:315(sample)
             3669428170  370.422    0.000  370.422    0.000 layer.py:203(isBlocking)
             1350336736  368.103    0.000  368.103    0.000 level.py:32(inverse)
                5591389  365.046    0.000  365.046    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             4476924369  355.428    0.000  355.428    0.000 {method 'random' of '_random.Random' objects}
               22995553   42.830    0.000  314.517    0.000 layer.py:69(restart)
               11178338  303.066    0.000  303.066    0.000 {built-in method torch._C._nn.mse_loss}
               55749398   35.936    0.000  284.846    0.000 flatten.py:39(forward)
               11180006  278.238    0.000  278.238    0.000 {built-in method max}
                5589169   21.744    0.000  265.623    0.000 exploration.py:47(epsilonGreedy)
              100605132  114.011    0.000  256.210    0.000 tensor.py:596(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550920: <Coconuts_teleport_0> in cluster <dcc> Done

Job <Coconuts_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:51 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 26 07:05:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 07:05:15 2021
Terminated at Tue Apr 27 07:00:37 2021
Results reported at Tue Apr 27 07:00:37 2021

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

    CPU time :                                   86092.10 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2671.58 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86153 sec.
    Turnaround time :                            571126 sec.

The output (if any) is above this job summary.

