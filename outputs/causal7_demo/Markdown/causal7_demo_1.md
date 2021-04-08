
# Parameters

    Name :                      causal7_demo-1
    Main :                      teleport
    Level :                     Levels.Causal7
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


      48841875041 function calls (48664504874 primitive calls) in 57305.47 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57305.469 57305.469 {built-in method builtins.exec}
                      1    1.866    1.866 57305.469 57305.469 <string>:1(<module>)
                      1  139.118  139.118 57303.603 57303.603 main.py:40(teleport)
                6335058   22.003    0.000 17756.309    0.003 agent.py:29(learn)
                6335058  427.467    0.000 14971.037    0.002 learner.py:42(Qlearn)
                3167529   13.467    0.000 13428.299    0.004 game.py:41(step)
                3167529   16.944    0.000 12751.357    0.004 layers.py:710(step)
                3167529  102.761    0.000 10728.282    0.003 agent.py:54(_learn)
                3167529 5690.500    0.002 9995.903    0.003 replaybuffer.py:28(teleporter_save_data)
        199540820/22171664  744.355    0.000 7300.815    0.000 module.py:715(_call_impl)
                3167529   84.360    0.000 6991.662    0.002 agent.py:117(_learn)
                3167529  259.467    0.000 6899.859    0.002 layers.py:17(step)
               15836606   39.212    0.000 6816.768    0.000 network.py:24(forward)
               15836606  176.156    0.000 6685.098    0.000 container.py:115(forward)
              316752900  508.874    0.000 6612.596    0.000 layer.py:98(move)
                3167529 4340.041    0.001 6579.673    0.002 agent.py:88(interveen)
                6335058   38.045    0.000 6113.180    0.001 grad_mode.py:23(decorate_context)
                6335058  200.339    0.000 6005.335    0.001 adam.py:55(step)
                3167530  444.991    0.000 5812.983    0.002 layers.py:676(update)
                6335058 1106.285    0.000 4948.284    0.001 functional.py:53(adam)
                6334019  134.606    0.000 4520.291    0.001 agent.py:49(__call__)
                3167529 2521.308    0.001 4079.122    0.001 replaybuffer.py:22(sample_data)
              316752900  629.510    0.000 3717.029    0.000 layers.py:727(check)
                6335058   37.080    0.000 3440.973    0.001 tensor.py:181(backward)
              330994620 3412.043    0.000 3412.043    0.000 {built-in method clone}
                6335058   21.331    0.000 3403.893    0.001 __init__.py:68(backward)
                6335058 3242.609    0.001 3242.609    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3167529 1560.490    0.000 2964.509    0.001 agent.py:67(modify)
               31673212   53.781    0.000 2464.346    0.000 conv.py:422(forward)
               31673212   59.853    0.000 2389.214    0.000 conv.py:414(_conv_forward)
               31673212 2318.186    0.000 2318.186    0.000 {built-in method conv2d}
               41174760   89.517    0.000 2146.136    0.000 linear.py:92(forward)
               41174760  155.592    0.000 2015.796    0.000 functional.py:1669(linear)
                4786122   47.016    0.000 1933.200    0.000 layers.py:731(restart)
              316752900  460.751    0.000 1887.991    0.000 layers.py:721(isFree)
              885284691  474.778    0.000 1581.988    0.000 {built-in method builtins.any}
               28506722 1559.654    0.000 1559.654    0.000 {built-in method cat}
                4786122   22.904    0.000 1543.340    0.000 level.py:8(__init__)
              399108708  923.594    0.000 1542.663    0.000 tensor.py:933(grad)
               22172710  886.530    0.000 1523.966    0.000 layer.py:167(NoRock_update)
                3167529   38.467    0.000 1436.362    0.000 agent.py:112(__call__)
             2194247692 1148.252    0.000 1427.240    0.000 layer.py:95(isFree)
               41174760 1421.109    0.000 1421.109    0.000 {built-in method addmm}
                9501548   59.753    0.000 1381.795    0.000 agent.py:59(modify_board)
                6335058  126.385    0.000 1338.738    0.000 optimizer.py:167(zero_grad)
                3167529   57.409    0.000 1329.187    0.000 replaybuffer.py:18(stacker)
                4786122   56.772    0.000 1311.329    0.000 levels.py:446(generate)
               22970293  218.327    0.000 1195.215    0.000 level.py:41(notUsed)
             4689337169  824.098    0.000 1173.874    0.000 enum.py:646(__hash__)
              114031044 1006.581    0.000 1006.581    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              340496168  947.805    0.000  947.805    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               13633993  942.516    0.000  942.516    0.000 {built-in method tensor}
               57011366   47.022    0.000  935.412    0.000 activation.py:713(forward)
                9501548  897.138    0.000  897.138    0.000 {built-in method torch._C._nn.one_hot}
              316752900  562.123    0.000  895.286    0.000 layers.py:625(check)
               57011366   74.668    0.000  888.390    0.000 functional.py:1292(leaky_relu)
              316752900  531.599    0.000  859.752    0.000 layers.py:610(check)
              316752900  525.187    0.000  855.245    0.000 layers.py:595(check)
              519472936  282.222    0.000  845.103    0.000 overrides.py:1070(has_torch_function)
              114031044  837.726    0.000  837.726    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               57011366  806.039    0.000  806.039    0.000 {built-in method torch._C._nn.leaky_relu}
             2495735024  643.038    0.000  787.165    0.000 layers.py:692(<genexpr>)
               22174489  114.773    0.000  776.260    0.000 tensor.py:21(wrapped)
              338927489  112.017    0.000  765.896    0.000 {built-in method builtins.all}
                6335058    6.815    0.000  726.183    0.000 game.py:37(board)
             1012622224  266.777    0.000  677.378    0.000 layers.py:682(<genexpr>)
                3167529  336.803    0.000  574.992    0.000 collector.py:53(collect)
               57015522  568.055    0.000  568.055    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               22970293   17.957    0.000  560.589    0.000 level.py:38(elementsIn)
               57015522  529.662    0.000  529.662    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             5307471255  506.770    0.000  506.770    0.000 layer.py:91(positions)
               57015522  470.547    0.000  470.547    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6334019  173.101    0.000  468.442    0.000 exploration.py:53(softmaxer)
               57015522  413.174    0.000  413.174    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              316752900  255.046    0.000  399.945    0.000 layers.py:581(check)
             1002337975  384.056    0.000  384.056    0.000 layer.py:146(elements)
               22970293  177.257    0.000  360.340    0.000 level.py:39(<listcomp>)
             4689360320  349.780    0.000  349.780    0.000 {built-in method builtins.hash}
               33502854   29.884    0.000  330.739    0.000 layer.py:69(restart)
             1102294488  252.165    0.000  315.527    0.000 overrides.py:1083(<genexpr>)
                6335058    8.974    0.000  310.614    0.000 loss.py:445(forward)
               57015522  307.508    0.000  307.508    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6335058   33.418    0.000  301.640    0.000 functional.py:2637(mse_loss)
               15837645  289.338    0.000  289.338    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        2719884069/2719884067  189.973    0.000  275.940    0.000 {built-in method builtins.len}
              481370993  197.418    0.000  274.621    0.000 layer.py:130(add)
               41174760  252.234    0.000  252.234    0.000 {method 't' of 'torch._C._TensorBase' objects}
                4786222  123.498    0.000  248.555    0.000 layers.py:30(reset)
             1102867227  247.357    0.000  247.357    0.000 level.py:32(inverse)
              318105928  155.343    0.000  231.435    0.000 layer.py:126(remove)
               19005174  229.869    0.000  229.869    0.000 {built-in method sum}
             2194247692  224.896    0.000  224.896    0.000 layer.py:203(isBlocking)
                3167529   82.591    0.000  223.234    0.000 random.py:315(sample)
                3168795  205.904    0.000  205.904    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                4786122  114.238    0.000  196.112    0.000 level.py:16(<dictcomp>)
              999232430  189.025    0.000  189.025    0.000 enum.py:352(<genexpr>)
               22970293  114.127    0.000  182.292    0.000 {built-in method _functools.reduce}
               98590358  120.318    0.000  181.370    0.000 layers.py:107(isDone)
                6335058  178.075    0.000  178.075    0.000 {built-in method torch._C._nn.mse_loss}
               31673212   23.100    0.000  170.374    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9501881: <causal7_demo_1> in cluster <dcc> Done

Job <causal7_demo_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Wed Apr  7 15:59:17 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr  7 20:57:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 20:57:25 2021
Terminated at Thu Apr  8 12:52:33 2021
Results reported at Thu Apr  8 12:52:33 2021

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

    CPU time :                                   57120.72 sec.
    Max Memory :                                 2816 MB
    Average Memory :                             2812.99 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13568.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57310 sec.
    Turnaround time :                            75196 sec.

The output (if any) is above this job summary.

