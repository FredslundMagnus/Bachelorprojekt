
# Parameters

    Name :                      test_METAk100000-0
    Main :                      metateleport
    Level :                     Levels.Causal1
    Hours :                     4.0
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
    Layer rock :                False
    Layer dirt :                False
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         100000.0
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      6229009472 function calls (6158270845 primitive calls) in 14117.81 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14117.814 14117.814 {built-in method builtins.exec}
                      1    5.114    5.114 14117.814 14117.814 <string>:1(<module>)
                      1   59.543   59.543 14112.700 14112.700 main.py:14(metateleport)
                2384127    8.324    0.000 5538.689    0.002 agent.py:27(learn)
                2384127  137.936    0.000 4455.131    0.002 learner.py:42(Qlearn)
                1589418   55.291    0.000 4149.723    0.003 agent.py:51(_learn)
                1589418 2536.946    0.002 3078.766    0.002 replaybuffer.py:23(sample_data)
        79280702/8543774  308.561    0.000 2466.937    0.000 module.py:866(_call_impl)
                6159647   17.533    0.000 2299.341    0.000 network.py:24(forward)
                6159647   74.877    0.000 2243.518    0.000 container.py:117(forward)
                2980811   68.057    0.000 1808.653    0.001 agent.py:46(__call__)
                2384127   19.503    0.000 1716.488    0.001 optimizer.py:84(wrapper)
                2384127   10.325    0.000 1630.352    0.001 grad_mode.py:24(decorate_context)
                2384127   67.819    0.000 1598.791    0.001 adam.py:55(step)
                 794709    3.365    0.000 1484.080    0.002 game.py:27(step)
                2384127  331.528    0.000 1452.612    0.001 _functional.py:53(adam)
                 794709   22.620    0.000 1374.822    0.002 agent.py:110(_learn)
                 794709    4.785    0.000 1360.362    0.002 layers.py:475(step)
                1589418  464.695    0.000 1299.447    0.001 agent.py:81(interveen)
                2384127    9.315    0.000 1156.152    0.000 tensor.py:195(backward)
                2384127    9.256    0.000 1146.518    0.000 __init__.py:68(backward)
                2384127 1093.338    0.000 1093.338    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1589418  605.717    0.000 1056.227    0.001 replaybuffer.py:27(teleporter_save_data)
                 794709  656.442    0.001 1022.389    0.001 agent.py:114(metamodify)
               12319294   26.103    0.000  831.033    0.000 conv.py:398(forward)
               12319294   19.127    0.000  790.770    0.000 conv.py:390(_conv_forward)
               12319294  771.642    0.000  771.642    0.000 {built-in method conv2d}
                 794709   65.785    0.000  678.078    0.001 layers.py:18(step)
                 794710   83.566    0.000  670.173    0.001 layers.py:446(update)
               16889523   33.078    0.000  630.937    0.000 linear.py:93(forward)
               79470900   81.703    0.000  604.827    0.000 layer.py:76(move)
               16889523   13.288    0.000  579.983    0.000 functional.py:1737(linear)
               16889523  563.611    0.000  563.611    0.000 {built-in method torch._C._nn.linear}
                4570229   37.854    0.000  552.660    0.000 agent.py:55(modify_board)
               14106737  500.059    0.000  500.059    0.000 {built-in method cat}
                1589418   37.744    0.000  430.380    0.000 replaybuffer.py:19(stacker)
               44160648  394.893    0.000  394.893    0.000 {built-in method clone}
                4570229  355.089    0.000  355.089    0.000 {built-in method torch._C._nn.one_hot}
               79470900   50.716    0.000  353.896    0.000 layers.py:486(isFree)
               23049170   23.105    0.000  333.651    0.000 activation.py:713(forward)
               23049170   18.380    0.000  310.547    0.000 functional.py:1364(leaky_relu)
                 794709   12.296    0.000  309.421    0.000 agent.py:105(__call__)
              222718230  269.233    0.000  303.180    0.000 layer.py:73(isFree)
               23049170  288.314    0.000  288.314    0.000 {built-in method torch._C._nn.leaky_relu}
               44503704  282.039    0.000  282.039    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2384127   45.284    0.000  254.648    0.000 optimizer.py:189(zero_grad)
               44503704  250.347    0.000  250.347    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2384130  127.513    0.000  211.762    0.000 layer.py:137(NoRock_update)
               79471000   20.563    0.000  207.551    0.000 {built-in method builtins.all}
                4098237  201.781    0.000  201.781    0.000 {built-in method tensor}
              238575159   54.015    0.000  195.565    0.000 layers.py:452(<genexpr>)
                2980811   67.463    0.000  177.202    0.000 exploration.py:53(softmaxer)
               22251852  168.599    0.000  168.599    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2384127    2.648    0.000  161.930    0.000 game.py:23(board)
                 794709   87.466    0.000  148.760    0.000 collector.py:54(collect)
               22251852  145.658    0.000  145.658    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 653624    4.878    0.000  136.508    0.000 layers.py:496(restart)
               79471000   92.556    0.000  135.009    0.000 layers.py:110(isDone)
               22251852  134.785    0.000  134.785    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               22251852  133.980    0.000  133.980    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              155763048   99.019    0.000  122.250    0.000 tensor.py:906(grad)
                1589418   41.969    0.000  108.488    0.000 random.py:315(sample)
                2384127    3.684    0.000  100.332    0.000 loss.py:527(forward)
               22251852   99.596    0.000   99.596    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2384127    9.650    0.000   96.648    0.000 functional.py:2898(mse_loss)
               47936168   95.601    0.000   95.601    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 653624    2.692    0.000   92.700    0.000 level.py:8(__init__)
                 653624    5.114    0.000   78.113    0.000 levels.py:122(generate)
               79470900   58.399    0.000   75.988    0.000 layers.py:492(check)
                7152381   70.595    0.000   70.595    0.000 {built-in method sum}
        600342471/600342468   53.561    0.000   70.281    0.000 {built-in method builtins.len}
                1960872   16.208    0.000   68.188    0.000 level.py:41(notUsed)
                2384127   58.399    0.000   58.399    0.000 {built-in method torch._C._nn.mse_loss}
                3973545    5.007    0.000   55.450    0.000 tensor.py:525(__rsub__)
                2980811   55.360    0.000   55.360    0.000 {built-in method multinomial}
               12319294    8.966    0.000   54.551    0.000 flatten.py:39(forward)
               93850081   39.475    0.000   54.158    0.000 layer.py:100(add)
              192124862   52.727    0.000   52.727    0.000 layer.py:116(elements)
                2384503   52.206    0.000   52.206    0.000 {built-in method max}
               71623665   33.326    0.000   49.718    0.000 layer.py:96(remove)
                3973545   49.528    0.000   49.528    0.000 {built-in method rsub}
               81454569   32.145    0.000   47.393    0.000 random.py:250(_randbelow_with_getrandbits)
                1589420   45.587    0.000   45.587    0.000 {built-in method nonzero}
               12319294   45.586    0.000   45.586    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               64583586   42.833    0.000   42.836    0.000 module.py:934(__getattr__)
                2384127    8.675    0.000   41.968    0.000 __init__.py:28(_make_grads)
               80870714   41.417    0.000   41.417    0.000 {built-in method torch._C._get_tracing_state}
                2384127   41.191    0.000   41.191    0.000 {built-in method gather}
                4768254    9.279    0.000   40.397    0.000 profiler.py:615(__enter__)
              469469830   39.869    0.000   39.869    0.000 layer.py:69(positions)
                1960872    2.130    0.000   38.083    0.000 layer.py:50(restart)
                3299106   37.888    0.000   37.888    0.000 {method 'long' of 'torch._C._TensorBase' objects}
                5562967   37.609    0.000   37.609    0.000 {built-in method zeros}
              135682667   24.920    0.000   35.855    0.000 enum.py:646(__hash__)
                4768254    6.546    0.000   35.220    0.000 profiler.py:607(__init__)
                2981108    3.025    0.000   32.713    0.000 functional.py:1553(softmax)
                 653724   16.153    0.000   32.402    0.000 layers.py:33(reset)
                 794709    3.351    0.000   32.271    0.000 exploration.py:47(epsilonGreedy)
                2384127   31.341    0.000   31.341    0.000 {built-in method ones_like}
                4768254   31.118    0.000   31.118    0.000 {built-in method torch._ops.profiler._record_function_enter}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9457744: <test_METAk100000_0> in cluster <dcc> Done

Job <test_METAk100000_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:24:28 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 17:24:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 17:24:29 2021
Terminated at Wed Mar 24 21:20:01 2021
Results reported at Wed Mar 24 21:20:01 2021

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

    CPU time :                                   14077.35 sec.
    Max Memory :                                 5111 MB
    Average Memory :                             4374.10 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3081.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14202 sec.
    Turnaround time :                            14133 sec.

The output (if any) is above this job summary.

