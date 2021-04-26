
# Parameters

    Name :                      Diamonds3_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal6
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


      80640719778 function calls (80414014087 primitive calls) in 86105.70 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.696 86105.696 {built-in method builtins.exec}
                      1    1.523    1.523 86105.696 86105.696 <string>:1(<module>)
                      1  183.494  183.494 86104.173 86104.173 main.py:45(teleport)
                8097146   27.668    0.000 27636.348    0.003 agent.py:29(learn)
                8097146  657.348    0.000 23668.524    0.003 learner.py:42(Qlearn)
                4048573   16.289    0.000 21351.570    0.005 game.py:41(step)
                4048573   22.045    0.000 20383.229    0.005 layers.py:718(step)
                4048573  131.689    0.000 16607.577    0.004 agent.py:54(_learn)
                4048573 7162.011    0.002 13694.488    0.003 replaybuffer.py:28(teleporter_save_data)
                4048573  113.238    0.000 10985.968    0.003 agent.py:117(_learn)
                4048573  297.429    0.000 10970.133    0.003 layers.py:17(step)
        255043407/28338727  971.368    0.000 10762.916    0.000 module.py:715(_call_impl)
              404857300  613.370    0.000 10639.890    0.000 layer.py:98(move)
                4048573 6914.477    0.002 10205.768    0.003 agent.py:88(interveen)
                8097146   46.549    0.000 10108.549    0.001 grad_mode.py:23(decorate_context)
               20241581   50.493    0.000 10076.404    0.000 network.py:27(forward)
                8097146  250.850    0.000 9973.536    0.001 adam.py:55(step)
               20241581  259.688    0.000 9910.987    0.000 container.py:115(forward)
                4048574  540.793    0.000 9363.368    0.002 layers.py:684(update)
                8097146 1830.853    0.000 8630.917    0.001 functional.py:53(adam)
              404857300 1369.550    0.000 6793.861    0.000 layers.py:735(check)
                8095862  181.235    0.000 6608.768    0.001 agent.py:49(__call__)
                8097146   48.808    0.000 5448.104    0.001 tensor.py:181(backward)
                8097146   27.566    0.000 5399.296    0.001 __init__.py:68(backward)
                8097146 5162.351    0.001 5162.351    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              368342921 5110.827    0.000 5110.827    0.000 {built-in method clone}
                4048573 3009.957    0.001 4871.533    0.001 replaybuffer.py:22(sample_data)
                4048573 2544.501    0.001 4636.032    0.001 agent.py:67(modify)
                9701782   84.341    0.000 4186.458    0.000 layers.py:740(restart)
               40483162   68.370    0.000 3611.139    0.000 conv.py:422(forward)
               40483162   77.988    0.000 3517.919    0.000 conv.py:414(_conv_forward)
                9701782   41.566    0.000 3444.382    0.000 level.py:8(__init__)
               40483162 3427.003    0.000 3427.003    0.000 {built-in method conv2d}
               52627597  116.030    0.000 3212.003    0.000 linear.py:92(forward)
               52627597  196.210    0.000 3045.919    0.000 functional.py:1669(linear)
                9701782  122.120    0.000 3038.675    0.000 levels.py:288(generate)
               58208987  495.919    0.000 2787.653    0.000 level.py:41(notUsed)
              404857300  694.965    0.000 2571.549    0.000 layers.py:729(isFree)
               52627597 2190.081    0.000 2190.081    0.000 {built-in method addmm}
               32388592 1264.591    0.000 2147.004    0.000 layer.py:167(NoRock_update)
             8774318182 1446.911    0.000 2095.378    0.000 enum.py:646(__hash__)
                4048573   53.531    0.000 2080.407    0.001 agent.py:112(__call__)
             1127941091  592.370    0.000 2060.709    0.000 {built-in method builtins.any}
              510120252 1307.105    0.000 2049.658    0.000 tensor.py:933(grad)
                8097146  186.649    0.000 1999.438    0.000 optimizer.py:167(zero_grad)
               12144435   87.661    0.000 1987.346    0.000 agent.py:59(modify_board)
               32387300 1946.733    0.000 1946.733    0.000 {built-in method cat}
             3212380052 1517.408    0.000 1876.583    0.000 layer.py:95(isFree)
              145748628 1802.890    0.000 1802.890    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4048573   71.283    0.000 1582.679    0.000 replaybuffer.py:18(stacker)
              404857300  927.657    0.000 1553.159    0.000 layers.py:424(check)
              380487356 1535.844    0.000 1535.844    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              145748628 1530.269    0.000 1530.269    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               72869178   56.487    0.000 1487.009    0.000 activation.py:713(forward)
               72869178   98.037    0.000 1430.523    0.000 functional.py:1292(leaky_relu)
               17337706 1345.236    0.000 1345.236    0.000 {built-in method tensor}
               72869178 1323.753    0.000 1323.753    0.000 {built-in method torch._C._nn.leaky_relu}
               58208987   39.239    0.000 1297.117    0.000 level.py:38(elementsIn)
               12144435 1249.899    0.000 1249.899    0.000 {built-in method torch._C._nn.one_hot}
              404857300  695.964    0.000 1119.328    0.000 layers.py:437(check)
             3556400562  879.192    0.000 1091.104    0.000 layers.py:700(<genexpr>)
               28342139  152.724    0.000 1079.130    0.000 tensor.py:21(wrapped)
              404857300  647.237    0.000 1066.434    0.000 layers.py:452(check)
                8097146    9.139    0.000 1027.818    0.000 game.py:37(board)
              663963583  342.904    0.000 1013.488    0.000 overrides.py:1070(has_torch_function)
               72874314  993.996    0.000  993.996    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4048573  568.902    0.000  954.560    0.000 collector.py:46(collect)
              433199539   95.944    0.000  938.571    0.000 {built-in method builtins.all}
               72874314  898.692    0.000  898.692    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              874854650  195.908    0.000  880.764    0.000 layers.py:690(<genexpr>)
             8922337751  838.387    0.000  838.387    0.000 layer.py:91(positions)
               58208987  411.160    0.000  837.827    0.000 level.py:39(<listcomp>)
               72874314  818.236    0.000  818.236    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72874314  734.209    0.000  734.209    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8095862  253.649    0.000  710.878    0.000 exploration.py:53(softmaxer)
              404857400  431.258    0.000  653.470    0.000 layers.py:113(isDone)
             8774347669  648.472    0.000  648.472    0.000 {built-in method builtins.hash}
               77614256   58.981    0.000  632.140    0.000 layer.py:69(restart)
             2761051828  602.709    0.000  602.709    0.000 level.py:32(inverse)
               72874314  571.917    0.000  571.917    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1575701036  541.578    0.000  541.578    0.000 layer.py:146(elements)
              404857300  320.792    0.000  493.244    0.000 layers.py:413(check)
              404857300  317.527    0.000  490.193    0.000 layers.py:402(check)
                9701882  232.834    0.000  464.460    0.000 layers.py:36(reset)
                8097146   11.305    0.000  460.628    0.000 loss.py:445(forward)
               20242865  451.372    0.000  451.372    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8097146   44.672    0.000  449.322    0.000 functional.py:2637(mse_loss)
        4687323631/4687323629  323.878    0.000  442.067    0.000 {built-in method builtins.len}
               52627597  430.384    0.000  430.384    0.000 {method 't' of 'torch._C._TensorBase' objects}
               58208987  263.225    0.000  420.051    0.000 {built-in method _functools.reduce}
             2444789210  414.503    0.000  414.503    0.000 enum.py:352(<genexpr>)
              760287337  286.636    0.000  397.581    0.000 layer.py:130(add)
              404857300  262.021    0.000  396.608    0.000 layers.py:23(check)
               24291438  384.588    0.000  384.588    0.000 {built-in method sum}
             1408896093  297.002    0.000  372.163    0.000 overrides.py:1083(<genexpr>)
                9701782  189.839    0.000  338.809    0.000 level.py:16(<dictcomp>)
              413019888  211.733    0.000  304.966    0.000 layer.py:126(remove)
             3212380052  291.254    0.000  291.254    0.000 layer.py:203(isBlocking)
                8097146  281.885    0.000  281.885    0.000 {built-in method torch._C._nn.mse_loss}
               40483162   29.842    0.000  277.545    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550902: <Diamonds3_teleport_0> in cluster <dcc> Done

Job <Diamonds3_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 07:19:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 07:19:26 2021
Terminated at Sat Apr 24 07:14:37 2021
Results reported at Sat Apr 24 07:14:37 2021

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

    CPU time :                                   85896.27 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2674.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86112 sec.
    Turnaround time :                            312769 sec.

The output (if any) is above this job summary.

