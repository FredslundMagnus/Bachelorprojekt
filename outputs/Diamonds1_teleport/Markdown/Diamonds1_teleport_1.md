
# Parameters

    Name :                      Diamonds1_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal2
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


      72473298753 function calls (72248979458 primitive calls) in 86113.53 seconds

##    Ordered by: cumulative time
   List reduced from 471 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.527 86113.527 {built-in method builtins.exec}
                      1    1.502    1.502 86113.527 86113.527 <string>:1(<module>)
                      1  177.515  177.515 86112.025 86112.025 main.py:45(teleport)
                8011906   27.447    0.000 28518.413    0.004 agent.py:29(learn)
                8011906  674.707    0.000 24484.462    0.003 learner.py:42(Qlearn)
                4005953   15.149    0.000 19363.383    0.005 game.py:41(step)
                4005953   21.038    0.000 18439.659    0.005 layers.py:718(step)
                4005953  132.229    0.000 17109.976    0.004 agent.py:54(_learn)
                4005953 7425.547    0.002 14449.788    0.004 replaybuffer.py:28(teleporter_save_data)
                4005953  111.053    0.000 11365.478    0.003 agent.py:117(_learn)
        252358698/28040414 1038.480    0.000 11103.876    0.000 module.py:715(_call_impl)
                4005953 7298.840    0.002 10688.305    0.003 agent.py:88(interveen)
                8011906   47.435    0.000 10580.757    0.001 grad_mode.py:23(decorate_context)
                8011906  271.731    0.000 10444.881    0.001 adam.py:55(step)
               20028508   52.165    0.000 10409.525    0.001 network.py:27(forward)
               20028508  271.331    0.000 10231.386    0.001 container.py:115(forward)
                4005953  312.317    0.000 9567.703    0.002 layers.py:17(step)
              400595300  665.528    0.000 9220.977    0.000 layer.py:98(move)
                8011906 1933.818    0.000 9038.825    0.001 functional.py:53(adam)
                4005954  563.186    0.000 8825.995    0.002 layers.py:684(update)
                8010649  176.949    0.000 6791.993    0.001 agent.py:49(__call__)
              400595300 1240.419    0.000 5725.953    0.000 layers.py:735(check)
                8011906   48.596    0.000 5527.956    0.001 tensor.py:181(backward)
              374905911 5480.761    0.000 5480.761    0.000 {built-in method clone}
                8011906   27.650    0.000 5479.360    0.001 __init__.py:68(backward)
                8011906 5239.155    0.001 5239.155    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4005953 2606.718    0.001 4738.731    0.001 agent.py:67(modify)
                4005953 2729.120    0.001 4597.364    0.001 replaybuffer.py:22(sample_data)
               10064713   80.137    0.000 3855.148    0.000 layers.py:740(restart)
               40057016   68.907    0.000 3684.780    0.000 conv.py:422(forward)
               40057016   75.568    0.000 3590.342    0.000 conv.py:414(_conv_forward)
               40057016 3501.534    0.000 3501.534    0.000 {built-in method conv2d}
               52073618  118.803    0.000 3323.449    0.000 linear.py:92(forward)
               52073618  201.759    0.000 3153.474    0.000 functional.py:1669(linear)
               10064713   38.838    0.000 3081.715    0.000 level.py:8(__init__)
               10064713  112.750    0.000 2663.359    0.000 levels.py:151(generate)
               48310134  444.773    0.000 2432.750    0.000 level.py:41(notUsed)
               52073618 2269.110    0.000 2269.110    0.000 {built-in method addmm}
              400595300  573.984    0.000 2206.365    0.000 layers.py:729(isFree)
                4005953   53.170    0.000 2133.564    0.001 agent.py:112(__call__)
              504750132 1353.047    0.000 2123.918    0.000 tensor.py:933(grad)
                8011906  206.028    0.000 2092.178    0.000 optimizer.py:167(zero_grad)
               12016602   86.651    0.000 2024.750    0.000 agent.py:59(modify_board)
               32046367 1966.678    0.000 1966.678    0.000 {built-in method cat}
             1115602084  591.220    0.000 1964.508    0.000 {built-in method builtins.any}
               28041678 1104.944    0.000 1892.293    0.000 layer.py:167(NoRock_update)
              144214308 1885.299    0.000 1885.299    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             6864693241 1191.516    0.000 1689.451    0.000 enum.py:646(__hash__)
              386922513 1661.067    0.000 1661.067    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2790792014 1287.654    0.000 1632.381    0.000 layer.py:95(isFree)
              144214308 1597.461    0.000 1597.461    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4005953   68.847    0.000 1583.792    0.000 replaybuffer.py:18(stacker)
               72102126   60.714    0.000 1536.721    0.000 activation.py:713(forward)
               72102126   94.032    0.000 1476.007    0.000 functional.py:1292(leaky_relu)
               72102126 1372.403    0.000 1372.403    0.000 {built-in method torch._C._nn.leaky_relu}
               12016602 1266.507    0.000 1266.507    0.000 {built-in method torch._C._nn.one_hot}
               17159445 1257.991    0.000 1257.991    0.000 {built-in method tensor}
               48310134   35.947    0.000 1141.083    0.000 level.py:38(elementsIn)
              400595300  710.722    0.000 1133.893    0.000 layers.py:219(check)
              428639173  197.933    0.000 1093.752    0.000 {built-in method builtins.all}
               28043773  155.311    0.000 1078.824    0.000 tensor.py:21(wrapped)
              400595300  656.456    0.000 1064.074    0.000 layers.py:231(check)
              656973966  356.922    0.000 1050.555    0.000 overrides.py:1070(has_torch_function)
              400595300  644.786    0.000 1048.119    0.000 layers.py:207(check)
               72107154 1033.314    0.000 1033.314    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4005953  591.527    0.000  993.180    0.000 collector.py:46(collect)
             3124245496  807.485    0.000  984.290    0.000 layers.py:700(<genexpr>)
               72107154  942.014    0.000  942.014    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8011906    8.901    0.000  937.887    0.000 game.py:37(board)
             1772065736  461.711    0.000  926.491    0.000 layers.py:690(<genexpr>)
               72107154  856.348    0.000  856.348    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72107154  766.965    0.000  766.965    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               48310134  367.305    0.000  740.550    0.000 level.py:39(<listcomp>)
                8010649  257.449    0.000  723.283    0.000 exploration.py:53(softmaxer)
               70452991   60.818    0.000  669.371    0.000 layer.py:69(restart)
             7223517935  664.466    0.000  664.466    0.000 layer.py:91(positions)
               72107154  599.922    0.000  599.922    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10064813  260.753    0.000  516.982    0.000 layers.py:36(reset)
              400595300  326.649    0.000  502.440    0.000 layers.py:196(check)
             6864722440  497.941    0.000  497.941    0.000 {built-in method builtins.hash}
             2319488286  497.041    0.000  497.041    0.000 level.py:32(inverse)
             1561282702  482.424    0.000  482.424    0.000 layer.py:146(elements)
                8011906   11.163    0.000  463.634    0.000 loss.py:445(forward)
               20029765  460.174    0.000  460.174    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8011906   42.591    0.000  452.472    0.000 functional.py:2637(mse_loss)
               52073618  442.794    0.000  442.794    0.000 {method 't' of 'torch._C._TensorBase' objects}
        4241054840/4241054838  318.377    0.000  440.373    0.000 {built-in method builtins.len}
              400595300  287.553    0.000  425.063    0.000 layers.py:23(check)
              757604364  294.832    0.000  407.927    0.000 layer.py:130(add)
               24035718  398.569    0.000  398.569    0.000 {built-in method sum}
             2101495982  384.202    0.000  384.202    0.000 enum.py:352(<genexpr>)
             1394064522  307.421    0.000  384.022    0.000 overrides.py:1083(<genexpr>)
               48310134  228.579    0.000  364.586    0.000 {built-in method _functools.reduce}
               10064713  194.444    0.000  355.274    0.000 level.py:16(<dictcomp>)
               40057016   29.305    0.000  287.492    0.000 flatten.py:39(forward)
              405993875  194.868    0.000  286.937    0.000 layer.py:126(remove)
                8011906  286.623    0.000  286.623    0.000 {built-in method torch._C._nn.mse_loss}
             3249027205  281.826    0.000  281.826    0.000 {method 'random' of '_random.Random' objects}
                4005953  102.730    0.000  277.300    0.000 random.py:315(sample)
             2790792014  274.882    0.000  274.882    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550897: <Diamonds1_teleport_1> in cluster <dcc> Done

Job <Diamonds1_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 06:33:42 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 06:33:42 2021
Terminated at Fri Apr 23 06:29:02 2021
Results reported at Fri Apr 23 06:29:02 2021

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

    CPU time :                                   85894.07 sec.
    Max Memory :                                 2675 MB
    Average Memory :                             2671.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86207 sec.
    Turnaround time :                            223634 sec.

The output (if any) is above this job summary.

