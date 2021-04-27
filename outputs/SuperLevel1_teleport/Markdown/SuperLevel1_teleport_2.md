
# Parameters

    Name :                      SuperLevel1_teleport-2
    Main :                      teleport
    Level :                     Levels.SuperLevel
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


      101356365570 function calls (101133471971 primitive calls) in 86112.20 seconds

##    Ordered by: cumulative time
   List reduced from 488 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.204 86112.204 {built-in method builtins.exec}
                      1    1.960    1.960 86112.204 86112.204 <string>:1(<module>)
                      1  256.276  256.276 86110.243 86110.243 main.py:45(teleport)
                3988148   23.522    0.000 35907.784    0.009 game.py:41(step)
                3988148   28.102    0.000 34610.947    0.009 layers.py:718(step)
                7976296   42.012    0.000 25052.271    0.003 agent.py:29(learn)
                3988148  420.851    0.000 24510.674    0.006 layers.py:17(step)
              398814800 1558.168    0.000 24054.285    0.000 layer.py:98(move)
                7976296  619.083    0.000 20826.889    0.003 learner.py:42(Qlearn)
              398814800 2663.075    0.000 16095.611    0.000 layers.py:735(check)
                3988148  169.992    0.000 15079.662    0.004 agent.py:54(_learn)
        250772649/27880061 1082.435    0.000 10422.448    0.000 module.py:715(_call_impl)
                3988149  627.739    0.000 10025.723    0.003 layers.py:684(update)
                3988148  138.988    0.000 9910.091    0.002 agent.py:117(_learn)
               19903765   53.646    0.000 9664.109    0.000 network.py:27(forward)
               19903765  268.282    0.000 9466.174    0.000 container.py:115(forward)
                7976296   68.374    0.000 8044.514    0.001 grad_mode.py:23(decorate_context)
                7976296  295.073    0.000 7859.621    0.001 adam.py:55(step)
                3988148 5604.870    0.001 7547.758    0.002 replaybuffer.py:22(sample_data)
                7939321  245.399    0.000 6516.311    0.001 agent.py:49(__call__)
                7976296 1451.338    0.000 6461.063    0.001 functional.py:53(adam)
              398814800 1099.748    0.000 5402.104    0.000 layers.py:729(isFree)
                3988148 2274.561    0.001 5388.522    0.001 agent.py:88(interveen)
                7976296   59.316    0.000 5118.932    0.001 tensor.py:181(backward)
                7976296   43.219    0.000 5059.617    0.001 __init__.py:68(backward)
                7976296 4791.353    0.001 4791.353    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51845937 2544.394    0.000 4325.108    0.000 layer.py:151(update)
             4902589871 3470.742    0.000 4302.356    0.000 layer.py:95(isFree)
                3988148 2336.865    0.001 4218.654    0.001 replaybuffer.py:28(teleporter_save_data)
                3988148 2107.155    0.001 4216.732    0.001 agent.py:67(modify)
               39807530   74.462    0.000 3590.788    0.000 conv.py:422(forward)
              398814800 2598.630    0.000 3586.243    0.000 layers.py:471(check)
               39807530   90.573    0.000 3482.371    0.000 conv.py:414(_conv_forward)
               39807530 3376.285    0.000 3376.285    0.000 {built-in method conv2d}
             1117133275  788.916    0.000 3142.678    0.000 {built-in method builtins.any}
               51734999  116.695    0.000 2992.293    0.000 linear.py:92(forward)
            11708504361 2085.942    0.000 2978.805    0.000 enum.py:646(__hash__)
               51734999  204.830    0.000 2812.680    0.000 functional.py:1669(linear)
              398814800 1795.922    0.000 2473.981    0.000 layers.py:77(check)
               11927469   97.186    0.000 2031.580    0.000 agent.py:59(modify_board)
                3988148   72.989    0.000 2005.696    0.001 agent.py:112(__call__)
               51734999 2004.977    0.000 2004.977    0.000 {built-in method addmm}
             5536969746 1631.352    0.000 1961.991    0.000 layers.py:700(<genexpr>)
              502506702 1175.561    0.000 1942.126    0.000 tensor.py:933(grad)
               31868209 1922.602    0.000 1922.602    0.000 {built-in method cat}
               17087009 1907.593    0.000 1907.593    0.000 {built-in method tensor}
              426735082  333.735    0.000 1706.082    0.000 {built-in method builtins.all}
                7976296  156.322    0.000 1688.258    0.000 optimizer.py:167(zero_grad)
                7976296   14.352    0.000 1596.474    0.000 game.py:37(board)
                3988148   83.865    0.000 1596.054    0.000 replaybuffer.py:18(stacker)
              132660066 1558.173    0.000 1558.173    0.000 {built-in method clone}
             3640557344  945.215    0.000 1401.456    0.000 layers.py:690(<genexpr>)
               11927469 1319.464    0.000 1319.464    0.000 {built-in method torch._C._nn.one_hot}
              143573328 1308.670    0.000 1308.670    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              398814800  854.787    0.000 1305.088    0.000 layers.py:286(check)
               71638764   67.613    0.000 1282.720    0.000 activation.py:713(forward)
            13820413851 1280.376    0.000 1280.376    0.000 layer.py:91(positions)
               71638764  109.958    0.000 1215.107    0.000 functional.py:1292(leaky_relu)
              398814800  733.669    0.000 1172.876    0.000 layers.py:246(check)
             1159859911 1169.975    0.000 1169.975    0.000 layer.py:146(elements)
               27920182  163.950    0.000 1145.763    0.000 tensor.py:21(wrapped)
               71638764 1095.479    0.000 1095.479    0.000 {built-in method torch._C._nn.leaky_relu}
              143573328 1056.847    0.000 1056.847    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              653947844  346.125    0.000 1048.847    0.000 overrides.py:1070(has_torch_function)
            11708533416  892.868    0.000  892.868    0.000 {built-in method builtins.hash}
                3988148  439.572    0.000  760.974    0.000 collector.py:46(collect)
                3317061   55.789    0.000  755.393    0.000 layers.py:740(restart)
               71786664  750.894    0.000  750.894    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              398814800  490.683    0.000  737.800    0.000 layers.py:273(check)
                7939321  248.153    0.000  709.400    0.000 exploration.py:53(softmaxer)
               71786664  703.849    0.000  703.849    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              398814800  451.083    0.000  692.562    0.000 layers.py:313(check)
              398814800  447.921    0.000  688.414    0.000 layers.py:141(check)
              398814800  491.019    0.000  674.822    0.000 layers.py:62(check)
               71786664  621.090    0.000  621.090    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              398814800  415.950    0.000  600.882    0.000 layers.py:124(check)
              398814800  375.594    0.000  554.523    0.000 layers.py:48(check)
               71786664  544.755    0.000  544.755    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        6399606135/6399606133  425.556    0.000  544.342    0.000 {built-in method builtins.len}
                7976296   15.859    0.000  503.190    0.000 loss.py:445(forward)
                7976296   59.246    0.000  487.331    0.000 functional.py:2637(mse_loss)
              398814800  316.209    0.000  458.331    0.000 layers.py:23(check)
             5597346531  456.300    0.000  456.300    0.000 {method 'random' of '_random.Random' objects}
              144587535  454.448    0.000  454.448    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3728979493  441.678    0.000  441.678    0.000 layer.py:203(isBlocking)
               19940740  408.998    0.000  408.998    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               71786664  404.178    0.000  404.178    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1387550076  311.308    0.000  385.568    0.000 overrides.py:1083(<genexpr>)
               51734999  367.683    0.000  367.683    0.000 {method 't' of 'torch._C._TensorBase' objects}
                3317061   23.484    0.000  346.833    0.000 level.py:8(__init__)
              528622436  250.602    0.000  344.247    0.000 layer.py:130(add)
                3989734  341.626    0.000  341.626    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               43121793   54.578    0.000  339.323    0.000 layer.py:69(restart)
                3988148  128.486    0.000  339.073    0.000 random.py:315(sample)
              351880812  221.005    0.000  331.849    0.000 layer.py:126(remove)
               23928888  319.327    0.000  319.327    0.000 {built-in method sum}
             4745974068  299.938    0.000  299.938    0.000 layer.py:84(isDead)
                7976296  281.452    0.000  281.452    0.000 {built-in method torch._C._nn.mse_loss}
              797629600  262.577    0.000  262.577    0.000 {method 'union' of 'set' objects}
                3988148   23.065    0.000  261.128    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550910: <SuperLevel1_teleport_2> in cluster <dcc> Done

Job <SuperLevel1_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 07:18:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 07:18:15 2021
Terminated at Sun Apr 25 07:13:33 2021
Results reported at Sun Apr 25 07:13:33 2021

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

    CPU time :                                   85903.45 sec.
    Max Memory :                                 2686 MB
    Average Memory :                             2682.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13698.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86218 sec.
    Turnaround time :                            399103 sec.

The output (if any) is above this job summary.

