
# Parameters

    Name :                      Rock_level-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
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
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      44813232353 function calls (44667033886 primitive calls) in 42917.27 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42917.274 42917.274 {built-in method builtins.exec}
                      1    0.982    0.982 42917.274 42917.274 <string>:1(<module>)
                      1  111.873  111.873 42916.292 42916.292 main.py:13(teleport)
                2610707    9.627    0.000 17649.443    0.007 game.py:27(step)
                2610707   12.379    0.000 17089.674    0.007 layers.py:373(step)
                5221414   18.400    0.000 11180.289    0.002 agent.py:26(learn)
                2610707  210.420    0.000 11121.888    0.004 layers.py:18(step)
              261070700  551.618    0.000 10889.123    0.000 layer.py:74(move)
                5221414  301.217    0.000 9423.438    0.002 learner.py:42(Qlearn)
              261070700  784.901    0.000 8101.196    0.000 layers.py:390(check)
                2610707   84.084    0.000 6650.224    0.003 agent.py:50(_learn)
                2610708  270.747    0.000 5937.904    0.002 layers.py:344(update)
                2610707 3057.198    0.001 5206.164    0.002 replaybuffer.py:27(teleporter_save_data)
        164472227/18274771  606.290    0.000 4962.534    0.000 module.py:866(_call_impl)
               13053357   34.995    0.000 4605.012    0.000 network.py:24(forward)
                2610707   72.361    0.000 4501.562    0.002 agent.py:101(_learn)
               13053357  147.922    0.000 4492.738    0.000 container.py:117(forward)
              261070700 3666.477    0.000 4345.587    0.000 layers.py:76(check)
                2610707 2150.181    0.001 3667.982    0.001 agent.py:77(interveen)
                5221414   41.260    0.000 3660.617    0.001 optimizer.py:84(wrapper)
                5221414   22.954    0.000 3475.838    0.001 grad_mode.py:24(decorate_context)
                5221414  136.705    0.000 3404.020    0.001 adam.py:55(step)
                5221414  707.744    0.000 3102.967    0.001 _functional.py:53(adam)
                5221236  112.499    0.000 3076.451    0.001 agent.py:45(__call__)
                9348069   80.958    0.000 2529.491    0.000 layers.py:394(restart)
                5221414   20.197    0.000 2434.325    0.000 tensor.py:195(backward)
                5221414   19.524    0.000 2413.409    0.000 __init__.py:68(backward)
               23496372 1608.236    0.000 2368.187    0.000 layer.py:119(update)
                5221414 2297.803    0.000 2297.803    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              261070700  430.399    0.000 1945.273    0.000 layers.py:384(isFree)
                2610707  968.838    0.000 1783.339    0.001 replaybuffer.py:23(sample_data)
              216763438 1769.084    0.000 1769.084    0.000 {built-in method clone}
               26106714   55.021    0.000 1692.363    0.000 conv.py:398(forward)
                2610707 1030.251    0.000 1669.873    0.001 agent.py:59(modify)
               26106714   33.528    0.000 1613.981    0.000 conv.py:390(_conv_forward)
                9348069   35.818    0.000 1582.549    0.000 level.py:8(__init__)
               26106714 1580.453    0.000 1580.453    0.000 {built-in method conv2d}
             2195873474 1250.684    0.000 1514.873    0.000 layer.py:71(isFree)
                9348069  224.808    0.000 1414.803    0.000 levels.py:95(generate)
               33938657   64.558    0.000 1249.604    0.000 linear.py:93(forward)
               33938657   26.282    0.000 1155.111    0.000 functional.py:1737(linear)
               33938657 1122.659    0.000 1122.659    0.000 {built-in method torch._C._nn.linear}
             4589903947  746.711    0.000 1082.293    0.000 enum.py:646(__hash__)
                2610707   32.402    0.000  954.661    0.000 agent.py:96(__call__)
                7831943   44.915    0.000  952.249    0.000 agent.py:54(modify_board)
               84132621  114.772    0.000  840.765    0.000 layer.py:48(restart)
               10794369  800.978    0.000  800.978    0.000 {built-in method tensor}
               18696138  111.324    0.000  797.791    0.000 level.py:41(notUsed)
               23496185  786.230    0.000  786.230    0.000 {built-in method cat}
              261070700  433.436    0.000  687.911    0.000 layers.py:216(check)
              261070800   77.129    0.000  670.110    0.000 {built-in method builtins.all}
                5221414    5.426    0.000  668.005    0.000 game.py:23(board)
               46992014   34.920    0.000  667.808    0.000 activation.py:713(forward)
              261070700  408.326    0.000  662.469    0.000 layers.py:230(check)
              261070700  397.371    0.000  644.327    0.000 layers.py:244(check)
                2610707   43.202    0.000  639.511    0.000 replaybuffer.py:19(stacker)
               46992014   36.224    0.000  632.887    0.000 functional.py:1364(leaky_relu)
                7831943  630.309    0.000  630.309    0.000 {built-in method torch._C._nn.one_hot}
              833544227  193.790    0.000  622.124    0.000 layers.py:350(<genexpr>)
               93985452  592.638    0.000  592.638    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46992014  589.526    0.000  589.526    0.000 {built-in method torch._C._nn.leaky_relu}
              261070700  384.814    0.000  584.561    0.000 layers.py:63(check)
             1224833431  430.223    0.000  581.459    0.000 layer.py:98(add)
               93985452  541.904    0.000  541.904    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5221414   95.314    0.000  539.663    0.000 optimizer.py:189(zero_grad)
             6116593277  539.624    0.000  539.624    0.000 layer.py:67(positions)
             2483708173  528.908    0.000  528.908    0.000 layer.py:114(elements)
              568328583  247.849    0.000  497.669    0.000 layer.py:94(remove)
                9348169  225.096    0.000  454.512    0.000 layers.py:33(reset)
              224595381  430.821    0.000  430.821    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11958776  152.057    0.000  424.330    0.000 random.py:315(sample)
              514143795  418.721    0.000  418.721    0.000 level.py:32(inverse)
              261070800  266.573    0.000  401.477    0.000 layers.py:110(isDone)
                2610707  212.046    0.000  361.513    0.000 collector.py:54(collect)
               46992726  358.357    0.000  358.357    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4589923138  335.586    0.000  335.586    0.000 {built-in method builtins.hash}
              261070700  213.531    0.000  327.785    0.000 layers.py:203(check)
                5221236  117.332    0.000  311.912    0.000 exploration.py:53(softmaxer)
               46992726  308.988    0.000  308.988    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               46992726  293.141    0.000  293.141    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               46992726  287.740    0.000  287.740    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              328949136  207.630    0.000  257.725    0.000 tensor.py:906(grad)
             3716290720  246.705    0.000  246.705    0.000 {method 'append' of 'list' objects}
              261070700  104.706    0.000  245.544    0.000 layers.py:99(<listcomp>)
                5221414    6.694    0.000  213.062    0.000 loss.py:527(forward)
        2655920521/2655920519  177.693    0.000  212.748    0.000 {built-in method builtins.len}
               46992726  210.734    0.000  210.734    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              364301492  142.887    0.000  206.457    0.000 random.py:250(_randbelow_with_getrandbits)
                5221414   19.534    0.000  206.367    0.000 functional.py:2898(mse_loss)
              568328583  204.425    0.000  204.425    0.000 {method 'remove' of 'list' objects}
               18696138   15.396    0.000  203.968    0.000 level.py:38(elementsIn)
             2195873474  201.090    0.000  201.090    0.000 layer.py:175(isBlocking)
               15664242  157.116    0.000  157.116    0.000 {built-in method sum}
                5221414  124.733    0.000  124.733    0.000 {built-in method torch._C._nn.mse_loss}
               18696138   58.188    0.000  114.198    0.000 level.py:39(<listcomp>)
                5222197  113.986    0.000  113.986    0.000 {built-in method max}
               26106714   16.157    0.000  113.955    0.000 flatten.py:39(forward)
                7832121   10.285    0.000  108.646    0.000 tensor.py:525(__rsub__)
                9348069   49.899    0.000  107.120    0.000 level.py:16(<dictcomp>)
               26106714   97.798    0.000   97.798    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9441981: <Rock_level_0> in cluster <dcc> Done

Job <Rock_level_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:11 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:12 2021
Terminated at Sat Mar 20 13:08:40 2021
Results reported at Sat Mar 20 13:08:40 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   42801.84 sec.
    Max Memory :                                 5990 MB
    Average Memory :                             4342.99 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2202.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42938 sec.
    Turnaround time :                            42929 sec.

The output (if any) is above this job summary.

