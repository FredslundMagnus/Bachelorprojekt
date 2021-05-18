
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH_2-0
    Main :                      Load_Cfagent
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Maze_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58306608584 function calls (57944605811 primitive calls) in 86043.35 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.678 86110.678 {built-in method builtins.exec}
                      1    4.227    4.227 86110.678 86110.678 <string>:1(<module>)
                      1  325.584  325.584 86106.451 86106.451 main.py:109(Load_Cfagent)
                2669290 2777.637    0.001 24401.412    0.009 agent.py:212(counterfact)
                8007870   35.139    0.000 20779.777    0.003 agent.py:29(learn)
                8007870  520.046    0.000 16775.797    0.002 learner.py:42(Qlearn)
                2669290   14.411    0.000 15505.811    0.006 game.py:42(step)
                2669290   17.870    0.000 14889.837    0.006 layers.py:827(step)
        401064248/39064296 1730.092    0.000 13480.923    0.000 module.py:866(_call_impl)
               31056426   86.742    0.000 12731.585    0.000 network.py:28(forward)
               31056426  401.426    0.000 12422.943    0.000 container.py:117(forward)
               94615798 9025.787    0.000 9025.787    0.000 {built-in method tensor}
               88728735   55.991    0.000 8910.484    0.000 game.py:38(board)
                6189337  123.184    0.000 8725.209    0.001 agent.py:176(choose_action)
                2669290  318.154    0.000 8086.174    0.003 agent.py:54(_learn)
               11520639  325.253    0.000 7710.037    0.001 agent.py:49(__call__)
                2669290  406.804    0.000 7430.836    0.003 layers.py:793(update)
                2669290  264.159    0.000 7416.244    0.003 layers.py:17(step)
                2669290  313.439    0.000 7397.342    0.003 agent.py:204(_learn)
              266315296  442.138    0.000 7127.582    0.000 layer.py:106(move)
                8007870   74.557    0.000 6415.309    0.001 optimizer.py:84(wrapper)
                8007870   40.022    0.000 6084.607    0.001 grad_mode.py:24(decorate_context)
                8007870  264.511    0.000 5956.357    0.001 adam.py:55(step)
                2669290 4893.753    0.002 5775.397    0.002 replaybuffer.py:22(sample_data)
                2669290 4780.531    0.002 5630.366    0.002 replaybuffer.py:67(sample_data)
                8007870 1231.611    0.000 5412.979    0.001 _functional.py:53(adam)
               85417264 2913.408    0.000 5245.776    0.000 layer.py:175(NoRock_update)
                2669290   83.408    0.000 5242.577    0.002 agent.py:117(_learn)
               62112852  141.837    0.000 4593.424    0.000 conv.py:398(forward)
                8007870   28.938    0.000 4516.090    0.001 tensor.py:195(backward)
                8007870   37.524    0.000 4486.025    0.001 __init__.py:68(backward)
               62112852  113.164    0.000 4377.457    0.000 conv.py:390(_conv_forward)
                8007870 4271.068    0.001 4271.068    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62112852 4264.292    0.000 4264.292    0.000 {built-in method conv2d}
                2669290 2495.281    0.001 4256.642    0.002 replaybuffer.py:28(teleporter_save_data)
                2669290 2164.820    0.001 3927.960    0.001 agent.py:88(interveen)
              266315296  939.102    0.000 3864.955    0.000 layers.py:844(check)
                4379260   64.325    0.000 3512.053    0.001 layers.py:849(restart)
               87830698  184.978    0.000 3483.174    0.000 linear.py:93(forward)
               87830698   71.946    0.000 3196.402    0.000 functional.py:1737(linear)
               87830698 3107.163    0.000 3107.163    0.000 {built-in method torch._C._nn.linear}
                4379260   37.691    0.000 3050.509    0.001 level.py:8(__init__)
                5968196  372.399    0.000 2722.914    0.000 levels.py:9(generate)
              266315296  423.803    0.000 2395.234    0.000 layers.py:838(isFree)
                2669290 1420.002    0.001 2135.021    0.001 agent.py:67(modify)
             1933548004 1702.878    0.000 1971.431    0.000 layer.py:103(isFree)
               14189929   94.060    0.000 1925.947    0.000 agent.py:59(modify_board)
              118887124  125.016    0.000 1855.809    0.000 activation.py:713(forward)
                6189337 1578.194    0.000 1819.267    0.000 agent.py:187(convert_values)
              173433775 1746.559    0.000 1746.559    0.000 {built-in method clone}
              118887124   98.197    0.000 1730.793    0.000 functional.py:1364(leaky_relu)
              118887124 1613.340    0.000 1613.340    0.000 {built-in method torch._C._nn.leaky_relu}
               40882829 1570.457    0.000 1570.457    0.000 {built-in method cat}
                2669290 1058.090    0.000 1372.502    0.001 replaybuffer.py:73(CF_save_data)
                2669290   52.801    0.000 1305.589    0.000 agent.py:172(__call__)
             1334696921 1305.500    0.000 1305.500    0.000 layer.py:154(elements)
               14189929 1275.227    0.000 1275.227    0.000 {built-in method torch._C._nn.one_hot}
                2669290   49.671    0.000 1151.828    0.000 agent.py:112(__call__)
              266315296  701.631    0.000 1139.447    0.000 layers.py:168(check)
              149480240 1054.415    0.000 1054.415    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              270557609  240.409    0.000 1038.353    0.000 {built-in method builtins.any}
               13137780  117.788    0.000 1000.562    0.000 level.py:41(notUsed)
              149480240  936.021    0.000  936.021    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8007870  164.117    0.000  914.523    0.000 optimizer.py:189(zero_grad)
             3360754371  630.957    0.000  909.221    0.000 enum.py:646(__hash__)
              266929000  132.534    0.000  855.823    0.000 {built-in method builtins.all}
                5968196  428.437    0.000  806.627    0.000 levels.py:75(RFS)
             2362947660  660.002    0.000  797.944    0.000 layers.py:809(<genexpr>)
               11520639  283.990    0.000  772.706    0.000 exploration.py:53(softmaxer)
            10713064570  697.292    0.000  772.076    0.000 {built-in method builtins.len}
             1444949656  391.905    0.000  757.299    0.000 layers.py:799(<genexpr>)
                2669290   52.299    0.000  664.096    0.000 replaybuffer.py:18(stacker)
                2669290   50.447    0.000  640.219    0.000 replaybuffer.py:63(stacker)
               74740120  617.658    0.000  617.658    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               21654232  209.003    0.000  538.446    0.000 random.py:315(sample)
               74740120  537.536    0.000  537.536    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74740120  512.514    0.000  512.514    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               74740120  503.558    0.000  503.558    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              266315296  290.943    0.000  465.937    0.000 layers.py:141(check)
              523180840  344.124    0.000  427.903    0.000 tensor.py:906(grad)
               13137780   13.670    0.000  415.577    0.000 level.py:38(elementsIn)
                2669290  242.514    0.000  414.613    0.000 collector.py:46(collect)
              266315296  278.310    0.000  408.553    0.000 layers.py:48(check)
              437460964  404.322    0.000  404.322    0.000 level.py:32(inverse)
             4386114825  400.140    0.000  400.140    0.000 layer.py:99(positions)
              343061923  299.895    0.000  398.277    0.000 layer.py:134(remove)
                8007870   14.797    0.000  391.085    0.000 loss.py:527(forward)
              266315296  259.089    0.000  386.952    0.000 layers.py:124(check)
               35034080   51.811    0.000  385.173    0.000 layer.py:77(restart)
              190292994  384.834    0.000  384.834    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8007870   37.414    0.000  376.288    0.000 functional.py:2898(mse_loss)
               74740120  363.485    0.000  363.485    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              584158599  237.884    0.000  348.537    0.000 layer.py:138(add)
               26401088  344.999    0.000  344.999    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               85417264  330.689    0.000  330.689    0.000 layer.py:186(<listcomp>)
               62112852   52.743    0.000  306.545    0.000 flatten.py:39(forward)
              416189346  204.228    0.000  302.236    0.000 random.py:250(_randbelow_with_getrandbits)
              266315296  192.470    0.000  288.254    0.000 layers.py:23(check)
             3360784978  278.270    0.000  278.270    0.000 {built-in method builtins.hash}
                5968196  142.649    0.000  271.581    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632952: <Maze_Conver4_3counterfactsNOCRASH_2_0> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:01 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:49:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:49:21 2021
Terminated at Thu May 13 15:44:37 2021
Results reported at Thu May 13 15:44:37 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85904.18 sec.
    Max Memory :                                 8417 MB
    Average Memory :                             5869.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7967.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            86616 sec.

The output (if any) is above this job summary.

