
# Parameters

    Name :                      teleport_normal-0
    Main :                      teleport
    Hours :                     16.0
    Batch :                     100
    Width :                     11
    Height :                    11
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
    K :                         100000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.1
    Replay size :               50000
    Sample size :               50
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      35403757296 function calls (35274153733 primitive calls) in 57068.84 seconds

##    Ordered by: cumulative time
   List reduced from 446 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57314.212 57314.212 {built-in method builtins.exec}
                      1    0.776    0.776 57314.212 57314.212 <string>:1(<module>)
                      1   91.518   91.518 57313.436 57313.436 main.py:10(teleport)
                4626956   15.676    0.000 15311.273    0.003 agent.py:26(learn)
                2313478  321.771    0.000 13803.707    0.006 collector.py:36(collect)
               11567390 12264.465    0.001 13434.295    0.001 {built-in method builtins.sum}
                4626956  362.043    0.000 13295.634    0.003 learner.py:42(Qlearn)
                2313478    8.385    0.000 11223.645    0.005 game.py:21(step)
                2313478   10.513    0.000 10754.627    0.005 layers.py:212(step)
                2313478   65.968    0.000 9109.384    0.004 agent.py:50(_learn)
                2313479  221.788    0.000 9009.395    0.004 layers.py:192(update)
               15507825   93.416    0.000 7078.040    0.000 layers.py:233(restart)
                2313478 3275.579    0.001 6211.356    0.003 replaybuffer.py:27(teleporter_save_data)
                2313478   58.188    0.000 6175.075    0.003 agent.py:101(_learn)
        145740742/16193702  550.013    0.000 6004.760    0.000 module.py:715(_call_impl)
                4626956   24.992    0.000 5703.037    0.001 grad_mode.py:23(decorate_context)
               11566746   27.564    0.000 5629.315    0.000 network.py:24(forward)
                4626956  142.978    0.000 5628.494    0.001 adam.py:55(step)
               15507825   16.435    0.000 5615.737    0.000 levels.py:8(__init__)
               15507825   44.937    0.000 5599.302    0.000 level.py:8(__init__)
               11566746  139.318    0.000 5533.696    0.000 container.py:115(forward)
               15507825 1061.736    0.000 5429.224    0.000 levels.py:11(generate)
                2313478 3212.905    0.001 5048.762    0.002 agent.py:77(interveen)
                4626956 1017.775    0.000 4842.343    0.001 functional.py:53(adam)
                4626312   90.907    0.000 3673.775    0.001 agent.py:45(__call__)
                4626956   26.805    0.000 3017.606    0.001 tensor.py:181(backward)
                4626956   14.709    0.000 2990.800    0.001 __init__.py:68(backward)
               15507825 1488.084    0.000 2907.423    0.000 levels.py:76(RFS)
                4626956 2859.311    0.001 2859.311    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2313478 1443.314    0.001 2515.249    0.001 agent.py:59(modify)
              171551271 2299.394    0.000 2299.394    0.000 {built-in method clone}
               23133492   38.506    0.000 2007.102    0.000 conv.py:422(forward)
               23133492   47.188    0.000 1953.344    0.000 conv.py:414(_conv_forward)
               23133492 1898.687    0.000 1898.687    0.000 {built-in method conv2d}
               30073282   68.789    0.000 1806.410    0.000 linear.py:92(forward)
                2313478  745.529    0.000 1769.802    0.001 replaybuffer.py:23(sample_data)
                2313478  143.183    0.000 1720.907    0.001 layers.py:17(step)
               30073282  109.895    0.000 1709.458    0.000 functional.py:1669(linear)
              231347800  202.984    0.000 1555.669    0.000 layer.py:66(move)
               46523475  111.464    0.000 1349.878    0.000 layer.py:40(restart)
               13881792   43.660    0.000 1233.689    0.000 tensor.py:576(__iter__)
               30073282 1231.851    0.000 1231.851    0.000 {built-in method addmm}
              291498282  778.331    0.000 1210.118    0.000 tensor.py:933(grad)
                4626956  111.183    0.000 1178.326    0.000 optimizer.py:167(zero_grad)
               13881792 1162.327    0.000 1162.327    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2313478   27.469    0.000 1122.710    0.000 agent.py:96(__call__)
                6939790   44.020    0.000 1110.458    0.000 agent.py:54(modify_board)
               18507180 1084.906    0.000 1084.906    0.000 {built-in method cat}
                6940437  714.185    0.000 1068.446    0.000 layer.py:90(update)
               83285208 1019.050    0.000 1019.050    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               15507925  502.711    0.000  961.604    0.000 layers.py:37(reset)
              231347800  143.465    0.000  935.742    0.000 layers.py:223(isFree)
                2313478   36.751    0.000  873.834    0.000 replaybuffer.py:19(stacker)
               83285208  867.166    0.000  867.166    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               41640028   32.622    0.000  827.728    0.000 activation.py:713(forward)
               41640028   55.870    0.000  795.106    0.000 functional.py:1292(leaky_relu)
              603620714  699.111    0.000  792.277    0.000 layer.py:63(isFree)
               41640028  734.080    0.000  734.080    0.000 {built-in method torch._C._nn.leaky_relu}
              178491061  709.974    0.000  709.974    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6939790  700.070    0.000  700.070    0.000 {built-in method torch._C._nn.one_hot}
             1488751200  463.081    0.000  695.323    0.000 levels.py:33(<genexpr>)
             1333719507  442.645    0.000  595.211    0.000 layer.py:76(add)
                9533880  592.537    0.000  592.537    0.000 {built-in method tensor}
              240602798   74.767    0.000  591.498    0.000 {built-in method builtins.all}
              372468694  194.280    0.000  565.690    0.000 overrides.py:1070(has_torch_function)
               41642604  553.767    0.000  553.767    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              708468341  163.822    0.000  537.323    0.000 layers.py:197(<genexpr>)
               41642604  502.056    0.000  502.056    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               41642604  459.122    0.000  459.122    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              387695625  160.730    0.000  456.911    0.000 random.py:285(choice)
                4626956    4.948    0.000  434.301    0.000 game.py:17(board)
               41642604  410.473    0.000  410.473    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4626312  140.709    0.000  391.075    0.000 exploration.py:53(softmaxer)
              231347900  235.070    0.000  354.436    0.000 layers.py:65(isDone)
              535089152  243.800    0.000  353.471    0.000 random.py:250(_randbelow_with_getrandbits)
              411795889  144.795    0.000  349.481    0.000 {built-in method builtins.any}
               41642604  336.264    0.000  336.264    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2666026763  310.223    0.000  310.223    0.000 layer.py:85(elements)
             1130801753  200.592    0.000  287.928    0.000 enum.py:646(__hash__)
              372187800  281.889    0.000  281.889    0.000 {method 'intersection_update' of 'set' objects}
                9254898   42.255    0.000  278.418    0.000 tensor.py:21(wrapped)
             3981425670  251.663    0.000  251.663    0.000 {method 'append' of 'list' objects}
                4626956    6.061    0.000  251.213    0.000 loss.py:445(forward)
               17821303  102.142    0.000  250.643    0.000 random.py:315(sample)
                4626956   24.710    0.000  245.152    0.000 functional.py:2637(mse_loss)
              372187800  243.018    0.000  243.018    0.000 levels.py:86(<listcomp>)
               30073282  237.943    0.000  237.943    0.000 {method 't' of 'torch._C._TensorBase' objects}
              231347800  160.502    0.000  208.319    0.000 layers.py:229(check)
             2007626358  202.782    0.000  202.782    0.000 {method 'add' of 'set' objects}
              784265106  162.953    0.000  201.943    0.000 overrides.py:1083(<genexpr>)
             1891967216  194.263    0.000  194.263    0.000 layer.py:100(grid)
             1121208812  188.397    0.000  188.397    0.000 {built-in method builtins.min}
              511758225  187.016    0.000  187.016    0.000 level.py:25(inverse)
             1123578452  182.493    0.000  182.493    0.000 {built-in method builtins.max}
        768877027/768877025   93.849    0.000  165.984    0.000 {built-in method builtins.len}
                6940434   33.757    0.000  165.927    0.000 tensor.py:506(__rsub__)
               23133492   15.943    0.000  154.249    0.000 flatten.py:39(forward)
                4626956  153.830    0.000  153.830    0.000 {built-in method torch._C._nn.mse_loss}
                6940434  147.447    0.000  147.447    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              159622534  140.702    0.000  140.702    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9367047: <teleport_normal_0> in cluster <dcc> Done

Job <teleport_normal_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Mar  6 16:12:40 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Mar  6 16:12:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar  6 16:12:41 2021
Terminated at Sun Mar  7 08:08:21 2021
Results reported at Sun Mar  7 08:08:21 2021

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

    CPU time :                                   57122.28 sec.
    Max Memory :                                 2390 MB
    Average Memory :                             2382.79 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5802.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57446 sec.
    Turnaround time :                            57341 sec.

The output (if any) is above this job summary.

