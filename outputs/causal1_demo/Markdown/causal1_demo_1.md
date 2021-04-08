
# Parameters

    Name :                      causal1_demo-1
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      39189057410 function calls (39027878891 primitive calls) in 57311.21 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57311.215 57311.215 {built-in method builtins.exec}
                      1    1.802    1.802 57311.215 57311.215 <string>:1(<module>)
                      1  138.580  138.580 57309.413 57309.413 main.py:40(teleport)
                5756760   20.265    0.000 19535.819    0.003 agent.py:29(learn)
                5756760  464.730    0.000 16693.773    0.003 learner.py:42(Qlearn)
                2878380   95.105    0.000 11760.945    0.004 agent.py:54(_learn)
                2878380 5755.733    0.002 10878.726    0.004 replaybuffer.py:28(teleporter_save_data)
                2878380   12.868    0.000 10280.814    0.004 game.py:41(step)
                2878380   16.533    0.000 9647.444    0.003 layers.py:710(step)
                2878380   80.320    0.000 7742.116    0.003 agent.py:117(_learn)
        181325187/20147679  687.518    0.000 7628.035    0.000 module.py:715(_call_impl)
               14390919   36.239    0.000 7147.777    0.000 network.py:24(forward)
                5756760   35.647    0.000 7093.912    0.001 grad_mode.py:23(decorate_context)
               14390919  182.798    0.000 7029.950    0.000 container.py:115(forward)
                5756760  180.001    0.000 6994.193    0.001 adam.py:55(step)
                2878380 4626.501    0.002 6954.531    0.002 agent.py:88(interveen)
                5756760 1284.471    0.000 6020.980    0.001 functional.py:53(adam)
                2878381  388.288    0.000 5251.283    0.002 layers.py:676(update)
                5755779  132.707    0.000 4702.654    0.001 agent.py:49(__call__)
                2878380  216.806    0.000 4359.307    0.002 layers.py:17(step)
              287838000  431.819    0.000 4114.021    0.000 layer.py:98(move)
              297255318 3999.986    0.000 3999.986    0.000 {built-in method clone}
                2878380 2384.677    0.001 3858.242    0.001 replaybuffer.py:22(sample_data)
                5756760   34.006    0.000 3846.602    0.001 tensor.py:181(backward)
                5756760   19.787    0.000 3812.596    0.001 __init__.py:68(backward)
                5756760 3642.069    0.001 3642.069    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2878380 1727.285    0.001 3196.045    0.001 agent.py:67(modify)
               28781838   49.397    0.000 2553.575    0.000 conv.py:422(forward)
               28781838   54.616    0.000 2485.475    0.000 conv.py:414(_conv_forward)
               28781838 2421.329    0.000 2421.329    0.000 {built-in method conv2d}
               37415997   84.784    0.000 2294.844    0.000 linear.py:92(forward)
               37415997  141.235    0.000 2172.720    0.000 functional.py:1669(linear)
                5907839   47.766    0.000 1960.028    0.000 layers.py:731(restart)
              287838000  444.901    0.000 1677.505    0.000 layers.py:727(check)
              287838000  359.650    0.000 1583.941    0.000 layers.py:721(isFree)
               37415997 1555.232    0.000 1555.232    0.000 {built-in method addmm}
               25904439 1523.876    0.000 1523.876    0.000 {built-in method cat}
                5907839   24.397    0.000 1519.469    0.000 level.py:8(__init__)
                2878380   39.092    0.000 1485.909    0.001 agent.py:112(__call__)
              362675934  941.904    0.000 1483.611    0.000 tensor.py:933(grad)
                5756760  137.378    0.000 1433.667    0.000 optimizer.py:167(zero_grad)
                8634159   60.812    0.000 1403.698    0.000 agent.py:59(modify_board)
                2878380   54.604    0.000 1270.968    0.000 replaybuffer.py:18(stacker)
                5907839   64.475    0.000 1267.571    0.000 levels.py:122(generate)
              103621680 1265.996    0.000 1265.996    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              802912315  388.489    0.000 1258.951    0.000 {built-in method builtins.any}
             1663114795  995.064    0.000 1224.291    0.000 layer.py:95(isFree)
               17270286  721.614    0.000 1222.414    0.000 layer.py:167(NoRock_update)
              305889477 1203.891    0.000 1203.891    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               23041760  202.373    0.000 1143.117    0.000 level.py:41(notUsed)
              103621680 1064.499    0.000 1064.499    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               51806916   45.339    0.000 1051.415    0.000 activation.py:713(forward)
               51806916   66.646    0.000 1006.077    0.000 functional.py:1292(leaky_relu)
               51806916  933.055    0.000  933.055    0.000 {built-in method torch._C._nn.leaky_relu}
                8634159  882.643    0.000  882.643    0.000 {built-in method torch._C._nn.one_hot}
               12419147  856.221    0.000  856.221    0.000 {built-in method tensor}
              307988350  125.898    0.000  798.064    0.000 {built-in method builtins.all}
               20150250  107.766    0.000  764.942    0.000 tensor.py:21(wrapped)
              472052536  251.578    0.000  738.887    0.000 overrides.py:1070(has_torch_function)
             1288462966  328.919    0.000  692.467    0.000 layers.py:682(<genexpr>)
               51810840  688.055    0.000  688.055    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2878380  401.161    0.000  673.437    0.000 collector.py:53(collect)
             2730793896  453.909    0.000  656.774    0.000 enum.py:646(__hash__)
                5756760    7.266    0.000  628.556    0.000 game.py:37(board)
               51810840  627.427    0.000  627.427    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1973511827  492.632    0.000  598.045    0.000 layers.py:692(<genexpr>)
               51810840  566.615    0.000  566.615    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               23041760   17.040    0.000  521.369    0.000 level.py:38(elementsIn)
               51810840  507.447    0.000  507.447    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5755779  177.135    0.000  504.798    0.000 exploration.py:53(softmaxer)
              287838000  276.601    0.000  442.938    0.000 layers.py:135(check)
               51810840  398.560    0.000  398.560    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               35447034   31.438    0.000  380.459    0.000 layer.py:69(restart)
              287838000  240.552    0.000  368.338    0.000 layers.py:118(check)
              287838000  232.554    0.000  352.832    0.000 layers.py:42(check)
               23041760  162.559    0.000  329.632    0.000 level.py:39(<listcomp>)
                5756760    7.484    0.000  321.850    0.000 loss.py:445(forward)
               14391900  315.079    0.000  315.079    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                5756760   30.175    0.000  314.366    0.000 functional.py:2637(mse_loss)
             1032553909  312.605    0.000  312.605    0.000 layer.py:146(elements)
               37415997  308.472    0.000  308.472    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5907939  143.053    0.000  286.631    0.000 layers.py:30(reset)
               17270280  269.320    0.000  269.320    0.000 {built-in method sum}
             1001670744  213.151    0.000  268.870    0.000 overrides.py:1083(<genexpr>)
             1062845107  266.209    0.000  266.209    0.000 level.py:32(inverse)
             3027893273  261.926    0.000  261.926    0.000 layer.py:91(positions)
              501836010  188.281    0.000  261.619    0.000 layer.py:130(add)
        2181271482/2181271480  161.480    0.000  244.664    0.000 {built-in method builtins.len}
                5907839  124.195    0.000  214.397    0.000 level.py:16(<dictcomp>)
              126411474  142.329    0.000  213.226    0.000 layers.py:107(isDone)
             2730814959  202.869    0.000  202.869    0.000 {built-in method builtins.hash}
                5756760  198.096    0.000  198.096    0.000 {built-in method torch._C._nn.mse_loss}
                2878380   73.161    0.000  197.396    0.000 random.py:315(sample)
               28781838   20.180    0.000  193.716    0.000 flatten.py:39(forward)
              280447755  130.447    0.000  191.853    0.000 layer.py:126(remove)
                2879530  189.306    0.000  189.306    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                5757622  178.454    0.000  178.454    0.000 {built-in method max}
             1042187018  177.035    0.000  177.035    0.000 enum.py:352(<genexpr>)
               23041760  107.700    0.000  174.697    0.000 {built-in method _functools.reduce}
               28781838  173.536    0.000  173.536    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9497204: <causal1_demo_1> in cluster <dcc> Done

Job <causal1_demo_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:36 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr  7 20:42:23 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 20:42:23 2021
Terminated at Thu Apr  8 12:37:40 2021
Results reported at Thu Apr  8 12:37:40 2021

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

    CPU time :                                   57166.30 sec.
    Max Memory :                                 2820 MB
    Average Memory :                             2816.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13564.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57317 sec.
    Turnaround time :                            228484 sec.

The output (if any) is above this job summary.

