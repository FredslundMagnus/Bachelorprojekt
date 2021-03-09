
# Parameters

    Name :                      9x9_gamme0.995-0
    Main :                      teleport
    Hours :                     10.0
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
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.995
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      29632467987 function calls (29463742028 primitive calls) in 35694.17 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35717.220 35717.220 {built-in method builtins.exec}
                      1    0.936    0.936 35717.219 35717.219 <string>:1(<module>)
                      1  122.326  122.326 35716.284 35716.284 main.py:10(teleport)
                6026566   22.137    0.000 13782.119    0.002 agent.py:26(learn)
                6026566  370.993    0.000 11609.849    0.002 learner.py:42(Qlearn)
                3013283   10.989    0.000 9300.866    0.003 game.py:21(step)
                3013283   14.696    0.000 8692.426    0.003 layers.py:212(step)
                3013283  107.011    0.000 8248.976    0.003 agent.py:50(_learn)
        189816354/21091406  772.661    0.000 6174.965    0.000 module.py:866(_call_impl)
               15064840   48.129    0.000 5730.946    0.000 network.py:24(forward)
                3013283  216.319    0.000 5642.216    0.002 layers.py:17(step)
               15064840  187.665    0.000 5586.085    0.000 container.py:117(forward)
                3013283   92.561    0.000 5500.130    0.002 agent.py:101(_learn)
              301328300  305.738    0.000 5398.892    0.000 layer.py:66(move)
                6026566   47.865    0.000 4580.572    0.001 optimizer.py:84(wrapper)
                6026566   26.204    0.000 4357.927    0.001 grad_mode.py:24(decorate_context)
                6026566  167.314    0.000 4275.555    0.001 adam.py:55(step)
                6026566  916.721    0.000 3909.646    0.001 _functional.py:53(adam)
                6024991  139.262    0.000 3793.919    0.001 agent.py:45(__call__)
                3013283 1603.303    0.001 3473.736    0.001 agent.py:77(interveen)
                3013283 1866.967    0.001 3282.793    0.001 replaybuffer.py:27(teleporter_save_data)
              301328300  639.813    0.000 3149.862    0.000 layers.py:229(check)
                3013284  272.904    0.000 3016.811    0.001 layers.py:192(update)
                6026566   24.484    0.000 2889.315    0.000 tensor.py:195(backward)
                6026566   24.514    0.000 2864.025    0.000 __init__.py:68(backward)
                6026566 2722.655    0.000 2722.655    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               30129680   69.843    0.000 2068.678    0.000 conv.py:398(forward)
               30129680   41.217    0.000 1969.448    0.000 conv.py:390(_conv_forward)
                3013283  998.583    0.000 1939.548    0.001 replaybuffer.py:23(sample_data)
               30129680 1928.231    0.000 1928.231    0.000 {built-in method conv2d}
                3013283 1052.992    0.000 1810.656    0.001 agent.py:59(modify)
              301328300  393.825    0.000 1680.295    0.000 layers.py:223(isFree)
               39167954   85.342    0.000 1557.031    0.000 linear.py:93(forward)
               39167954   34.220    0.000 1433.263    0.000 functional.py:1737(linear)
               39167954 1391.092    0.000 1391.092    0.000 {built-in method torch._C._nn.linear}
             1773550826 1039.994    0.000 1286.470    0.000 layer.py:63(isFree)
              126538506 1215.368    0.000 1215.368    0.000 {built-in method clone}
                3013283   41.821    0.000 1202.090    0.000 agent.py:96(__call__)
                9038274   53.527    0.000 1130.746    0.000 agent.py:54(modify_board)
              301328300  665.282    0.000 1103.590    0.000 layers.py:124(check)
                1522649   15.461    0.000  987.572    0.001 layers.py:233(restart)
               24104689  912.399    0.000  912.399    0.000 {built-in method cat}
               24106272  351.754    0.000  894.815    0.000 layer.py:90(update)
               12729977  862.537    0.000  862.537    0.000 {built-in method tensor}
               54232794   46.276    0.000  843.365    0.000 activation.py:713(forward)
                1522649    3.043    0.000  835.449    0.001 levels.py:8(__init__)
                1522649   11.485    0.000  832.406    0.001 level.py:8(__init__)
                2077607  124.540    0.000  798.802    0.000 levels.py:11(generate)
               54232794   47.529    0.000  797.089    0.000 functional.py:1364(leaky_relu)
              301328400   98.607    0.000  779.249    0.000 {built-in method builtins.all}
              108478188  746.752    0.000  746.752    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54232794  739.711    0.000  739.711    0.000 {built-in method torch._C._nn.leaky_relu}
                9038274  737.184    0.000  737.184    0.000 {built-in method torch._C._nn.one_hot}
                3013283   46.244    0.000  726.001    0.000 replaybuffer.py:19(stacker)
              910288581  214.114    0.000  716.413    0.000 layers.py:197(<genexpr>)
                6026566    6.088    0.000  694.251    0.000 game.py:17(board)
             2563190337  483.042    0.000  687.689    0.000 enum.py:646(__hash__)
                6026566  120.177    0.000  683.423    0.000 optimizer.py:189(zero_grad)
              108478188  671.654    0.000  671.654    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              301328300  330.877    0.000  524.787    0.000 layers.py:95(check)
              301328400  310.158    0.000  476.195    0.000 layers.py:65(isDone)
                3013283  268.841    0.000  456.181    0.000 collector.py:37(collect)
               54239094  446.173    0.000  446.173    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4623161672  411.041    0.000  411.041    0.000 layer.py:59(positions)
              301328300  263.249    0.000  395.717    0.000 layers.py:50(check)
              792263856  394.344    0.000  394.344    0.000 layer.py:85(elements)
               54239094  391.996    0.000  391.996    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              301328300  252.916    0.000  389.942    0.000 layers.py:77(check)
                6024991  144.493    0.000  379.571    0.000 exploration.py:53(softmaxer)
               54239094  362.622    0.000  362.622    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54239094  359.564    0.000  359.564    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              379673712  247.800    0.000  313.363    0.000 tensor.py:906(grad)
              135576780  277.463    0.000  277.463    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               54239094  275.650    0.000  275.650    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2077607  144.955    0.000  275.552    0.000 levels.py:76(RFS)
                6026566    9.333    0.000  261.262    0.000 loss.py:527(forward)
                6026566   24.657    0.000  251.929    0.000 functional.py:2898(mse_loss)
                8691146   96.065    0.000  251.726    0.000 random.py:315(sample)
              372742031  150.762    0.000  205.032    0.000 layer.py:76(add)
             2563212408  204.651    0.000  204.651    0.000 {built-in method builtins.hash}
              285284485  132.678    0.000  195.246    0.000 layer.py:72(remove)
               18079698  194.589    0.000  194.589    0.000 {built-in method sum}
                4567947   25.864    0.000  192.677    0.000 level.py:41(notUsed)
             1559429663  157.534    0.000  157.534    0.000 layer.py:125(isBlocking)
                6026566  155.238    0.000  155.238    0.000 {built-in method torch._C._nn.mse_loss}
        902384669/902384667  110.814    0.000  153.742    0.000 {built-in method builtins.len}
                6027469  140.962    0.000  140.962    0.000 {built-in method max}
               30129680   21.254    0.000  140.001    0.000 flatten.py:39(forward)
              152150559  135.140    0.000  135.140    0.000 level.py:32(inverse)
                9039849   13.058    0.000  133.119    0.000 tensor.py:525(__rsub__)
               12181192   17.498    0.000  132.286    0.000 layer.py:40(restart)
              200505716   89.281    0.000  129.743    0.000 random.py:250(_randbelow_with_getrandbits)
                3013283   11.377    0.000  121.323    0.000 exploration.py:47(epsilonGreedy)
               30129680  118.747    0.000  118.747    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6024991  118.473    0.000  118.473    0.000 {built-in method multinomial}
                9039849  117.926    0.000  117.926    0.000 {built-in method rsub}
                6026566   24.125    0.000  111.772    0.000 __init__.py:28(_make_grads)
             1395028885  111.127    0.000  111.127    0.000 {method 'append' of 'list' objects}
                6026566  108.466    0.000  108.466    0.000 {built-in method gather}
              192830841  107.833    0.000  107.833    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9395484: <9x9_gamme0.995_0> in cluster <dcc> Done

Job <9x9_gamme0.995_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:59 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 03:08:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 03:08:51 2021
Terminated at Tue Mar  9 13:04:29 2021
Results reported at Tue Mar  9 13:04:29 2021

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

    CPU time :                                   35613.71 sec.
    Max Memory :                                 6569 MB
    Average Memory :                             4433.10 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1623.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35737 sec.
    Turnaround time :                            42570 sec.

The output (if any) is above this job summary.

