
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH_2-2
    Main :                      Load_Cfagent
    Level :                     Levels.Causal3
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
    Num :                       2
    Load name :                 Causal3_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64094758461 function calls (63683816936 primitive calls) in 86154.46 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86154.459 86154.459 {built-in method builtins.exec}
                      1    4.312    4.312 86154.459 86154.459 <string>:1(<module>)
                      1  317.124  317.124 86150.147 86150.147 main.py:109(Load_Cfagent)
                2896470 3349.165    0.001 26488.576    0.009 agent.py:212(counterfact)
                8689410   30.942    0.000 20412.682    0.002 agent.py:29(learn)
                8689410  508.352    0.000 16603.855    0.002 learner.py:42(Qlearn)
                2896470   12.998    0.000 14907.621    0.005 game.py:42(step)
                2896470   17.875    0.000 14303.241    0.005 layers.py:827(step)
        454838496/43899792 1799.015    0.000 14008.592    0.000 module.py:866(_call_impl)
               35210382   94.261    0.000 13282.623    0.000 network.py:28(forward)
               35210382  420.647    0.000 12960.451    0.000 container.py:117(forward)
                7471372  135.617    0.000 9729.932    0.001 agent.py:176(choose_action)
              109301191 9699.218    0.000 9699.218    0.000 {built-in method tensor}
              102912628   58.804    0.000 9592.316    0.000 game.py:38(board)
                2896470  245.205    0.000 8332.111    0.003 layers.py:17(step)
              289584220  455.407    0.000 8062.729    0.000 layer.py:106(move)
               13256660  330.434    0.000 8048.281    0.001 agent.py:49(__call__)
                2896470  292.169    0.000 7925.958    0.003 agent.py:54(_learn)
                2896470  291.101    0.000 7280.230    0.003 agent.py:204(_learn)
                8689410   69.658    0.000 6446.462    0.001 optimizer.py:84(wrapper)
                8689410   37.146    0.000 6128.609    0.001 grad_mode.py:24(decorate_context)
                8689410  264.588    0.000 6011.600    0.001 adam.py:55(step)
                2896470  409.738    0.000 5930.683    0.002 layers.py:793(update)
                8689410 1235.480    0.000 5458.822    0.001 _functional.py:53(adam)
                2896470   86.127    0.000 5154.246    0.002 agent.py:117(_learn)
                2896470 4306.307    0.001 5152.605    0.002 replaybuffer.py:22(sample_data)
                2896470 4294.267    0.001 5117.387    0.002 replaybuffer.py:67(sample_data)
               92687024 2741.480    0.000 4992.446    0.000 layer.py:175(NoRock_update)
               70420764  154.607    0.000 4757.160    0.000 conv.py:398(forward)
              289584220  986.034    0.000 4744.774    0.000 layers.py:844(check)
               70420764  104.427    0.000 4525.103    0.000 conv.py:390(_conv_forward)
               70420764 4420.676    0.000 4420.676    0.000 {built-in method conv2d}
                8689410   30.966    0.000 4351.089    0.001 tensor.py:195(backward)
                8689410   34.652    0.000 4318.976    0.000 __init__.py:68(backward)
                2896470 2343.595    0.001 4127.179    0.001 replaybuffer.py:28(teleporter_save_data)
                8689410 4120.200    0.000 4120.200    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2896470 2030.596    0.001 3785.269    0.001 agent.py:88(interveen)
               99838206  189.285    0.000 3640.983    0.000 linear.py:93(forward)
               99838206   84.388    0.000 3345.146    0.000 functional.py:1737(linear)
               99838206 3241.446    0.000 3241.446    0.000 {built-in method torch._C._nn.linear}
              289584220  433.228    0.000 2425.290    0.000 layers.py:838(isFree)
                6710985   65.291    0.000 2131.783    0.000 layers.py:849(restart)
                2896470 1415.648    0.000 2103.985    0.001 agent.py:67(modify)
                7471372 1738.446    0.000 2001.454    0.000 agent.py:187(convert_values)
             2187359411 1663.410    0.000 1992.062    0.000 layer.py:103(isFree)
               16153130   93.185    0.000 1977.098    0.000 agent.py:59(modify_board)
              135048588  122.715    0.000 1952.484    0.000 activation.py:713(forward)
              197175850 1864.999    0.000 1864.999    0.000 {built-in method clone}
              135048588  112.081    0.000 1829.769    0.000 functional.py:1364(leaky_relu)
              135048588 1695.551    0.000 1695.551    0.000 {built-in method torch._C._nn.leaky_relu}
                2896470 1258.481    0.000 1685.572    0.001 replaybuffer.py:73(CF_save_data)
               45117830 1557.233    0.000 1557.233    0.000 {built-in method cat}
                6710985   31.214    0.000 1545.608    0.000 level.py:8(__init__)
               16153130 1303.173    0.000 1303.173    0.000 {built-in method torch._C._nn.one_hot}
                2896470   48.285    0.000 1251.469    0.000 agent.py:172(__call__)
             1463427622 1227.059    0.000 1227.059    0.000 layer.py:154(elements)
                6710985  131.182    0.000 1219.580    0.000 levels.py:164(generate)
             4919570283  834.430    0.000 1216.563    0.000 enum.py:646(__hash__)
                2896470   45.024    0.000 1162.816    0.000 agent.py:112(__call__)
              162202320 1070.189    0.000 1070.189    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              291625424  240.392    0.000 1021.148    0.000 {built-in method builtins.any}
              289584220  606.484    0.000  977.777    0.000 layers.py:286(check)
                8689410  176.935    0.000  958.359    0.000 optimizer.py:189(zero_grad)
              162202320  952.340    0.000  952.340    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              289584220  542.424    0.000  925.675    0.000 layers.py:246(check)
               13421970  123.888    0.000  913.560    0.000 level.py:41(notUsed)
            11897791702  711.726    0.000  791.348    0.000 {built-in method builtins.len}
               13256660  294.147    0.000  789.345    0.000 exploration.py:53(softmaxer)
              289647000   91.758    0.000  783.992    0.000 {built-in method builtins.all}
             2546424135  643.829    0.000  780.757    0.000 layers.py:809(<genexpr>)
             1000241695  253.790    0.000  725.765    0.000 layers.py:799(<genexpr>)
                2896470   49.013    0.000  639.136    0.000 replaybuffer.py:18(stacker)
               81101160  628.297    0.000  628.297    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2896470   50.639    0.000  623.069    0.000 replaybuffer.py:63(stacker)
               81101160  540.591    0.000  540.591    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               19214910  197.797    0.000  518.641    0.000 random.py:315(sample)
             5641485092  513.467    0.000  513.467    0.000 layer.py:99(positions)
               81101160  507.877    0.000  507.877    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               81101160  504.475    0.000  504.475    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               53687880   64.203    0.000  503.257    0.000 layer.py:77(restart)
              289584220  303.532    0.000  489.424    0.000 layers.py:313(check)
              289584220  289.227    0.000  454.312    0.000 layers.py:273(check)
              567708120  359.422    0.000  446.360    0.000 tensor.py:906(grad)
               40408274  433.506    0.000  433.506    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2896470  246.917    0.000  419.300    0.000 collector.py:46(collect)
              216225450  403.493    0.000  403.493    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               13421970   13.380    0.000  395.746    0.000 level.py:38(elementsIn)
              289584220  258.690    0.000  390.591    0.000 layers.py:48(check)
             4919603466  382.138    0.000  382.138    0.000 {built-in method builtins.hash}
               81101160  378.098    0.000  378.098    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8689410   13.462    0.000  356.317    0.000 loss.py:527(forward)
                8689410   33.064    0.000  342.855    0.000 functional.py:2898(mse_loss)
              195550655  229.572    0.000  336.660    0.000 layers.py:113(isDone)
              642312730  239.042    0.000  333.056    0.000 layer.py:138(add)
               70420764   55.286    0.000  322.589    0.000 flatten.py:39(forward)
                6710985  160.996    0.000  319.548    0.000 layers.py:36(reset)
               92687024  319.310    0.000  319.310    0.000 layer.py:186(<listcomp>)
              304647838  226.658    0.000  305.868    0.000 layer.py:134(remove)
              289584220  202.087    0.000  300.527    0.000 layers.py:23(check)
              440262668  282.009    0.000  282.009    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632963: <Causal3_Conver4_3counterfactsNOCRASH_2_2> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:03 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May 16 23:26:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:26:17 2021
Terminated at Mon May 17 23:22:19 2021
Results reported at Mon May 17 23:22:19 2021

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

    CPU time :                                   85906.41 sec.
    Max Memory :                                 8857 MB
    Average Memory :                             6066.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7527.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86254 sec.
    Turnaround time :                            459676 sec.

The output (if any) is above this job summary.

