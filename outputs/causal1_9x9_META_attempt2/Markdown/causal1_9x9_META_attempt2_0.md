
# Parameters

    Name :                      causal1_9x9_META_attempt2-0
    Main :                      metateleport
    Level :                     Levels.Causal1
    Hours :                     11.0
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
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         200000
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
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      16176826881 function calls (16037417574 primitive calls) in 39316.85 seconds

##    Ordered by: cumulative time
   List reduced from 468 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39316.849 39316.849 {built-in method builtins.exec}
                      1    5.385    5.385 39316.849 39316.849 <string>:1(<module>)
                      1  132.677  132.677 39311.464 39311.464 main.py:14(metateleport)
                4556577   17.595    0.000 15152.534    0.003 agent.py:27(learn)
                4556577  367.892    0.000 12510.028    0.003 learner.py:42(Qlearn)
                3037718  116.790    0.000 11316.780    0.004 agent.py:51(_learn)
                3037718 5101.806    0.002 6338.053    0.002 replaybuffer.py:23(sample_data)
        156087772/16680164  714.502    0.000 6319.155    0.000 module.py:866(_call_impl)
               12123587   37.038    0.000 5916.283    0.000 network.py:24(forward)
               12123587  186.662    0.000 5795.196    0.000 container.py:117(forward)
                4556577   42.924    0.000 5245.613    0.001 optimizer.py:84(wrapper)
                4556577   20.809    0.000 5047.372    0.001 grad_mode.py:24(decorate_context)
                1518859    7.718    0.000 5025.009    0.003 game.py:27(step)
                4556577  149.563    0.000 4978.538    0.001 adam.py:55(step)
                6048151  169.758    0.000 4754.260    0.001 agent.py:46(__call__)
                1518859   10.546    0.000 4692.785    0.003 layers.py:475(step)
                4556577 1038.675    0.000 4658.721    0.001 _functional.py:53(adam)
                3037718 2325.406    0.001 4295.029    0.001 replaybuffer.py:27(teleporter_save_data)
                3037718 1843.296    0.001 4197.180    0.001 agent.py:81(interveen)
                1518859   49.686    0.000 3806.282    0.003 agent.py:146(_learn)
                4556577   21.047    0.000 3148.715    0.001 tensor.py:195(backward)
                4556577   18.828    0.000 3126.922    0.001 __init__.py:68(backward)
                4556577 2998.117    0.001 2998.117    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1518859  134.221    0.000 2952.497    0.002 layers.py:18(step)
              151885900  368.863    0.000 2804.047    0.000 layer.py:76(move)
                1518859 1683.121    0.001 2633.838    0.002 agent.py:101(metamodify)
               24247174   60.116    0.000 2064.436    0.000 conv.py:398(forward)
               24247174   34.806    0.000 1978.071    0.000 conv.py:390(_conv_forward)
               24247174 1943.265    0.000 1943.265    0.000 {built-in method conv2d}
                1518860  174.117    0.000 1715.754    0.001 layers.py:446(update)
               33333043   79.444    0.000 1685.637    0.000 linear.py:93(forward)
              119863066 1651.236    0.000 1651.236    0.000 {built-in method clone}
               33333043   31.390    0.000 1569.864    0.000 functional.py:1737(linear)
               33333043 1531.357    0.000 1531.357    0.000 {built-in method torch._C._nn.linear}
                9085869   94.069    0.000 1409.503    0.000 agent.py:55(modify_board)
               27312177 1232.105    0.000 1232.105    0.000 {built-in method cat}
              151885900  278.766    0.000 1139.481    0.000 layers.py:492(check)
              151885900  219.344    0.000 1037.389    0.000 layers.py:486(isFree)
                3037718   70.566    0.000 1005.027    0.000 replaybuffer.py:19(stacker)
               85056104  948.880    0.000  948.880    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45456630   40.260    0.000  939.096    0.000 activation.py:713(forward)
               45456630   40.881    0.000  898.836    0.000 functional.py:1364(leaky_relu)
                9085869  872.724    0.000  872.724    0.000 {built-in method torch._C._nn.one_hot}
               45456630  849.440    0.000  849.440    0.000 {built-in method torch._C._nn.leaky_relu}
               85056104  831.165    0.000  831.165    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              825809725  679.043    0.000  818.045    0.000 layer.py:73(isFree)
                9113160  456.614    0.000  763.249    0.000 layer.py:121(update)
                1518859   28.704    0.000  758.459    0.000 agent.py:141(__call__)
                4556577  122.993    0.000  748.878    0.000 optimizer.py:189(zero_grad)
                7835857  579.520    0.000  579.520    0.000 {built-in method tensor}
               42528052  515.240    0.000  515.240    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6048151  175.306    0.000  483.880    0.000 exploration.py:53(softmaxer)
                4556577    6.079    0.000  473.406    0.000 game.py:23(board)
                1518859  280.463    0.000  464.491    0.000 collector.py:54(collect)
               42528052  453.759    0.000  453.759    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42528052  434.314    0.000  434.314    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              127430076  431.308    0.000  431.308    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              151886000   44.384    0.000  425.180    0.000 {built-in method builtins.all}
               42528052  422.848    0.000  422.848    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              458184390  112.659    0.000  399.724    0.000 layers.py:452(<genexpr>)
              151885900  262.708    0.000  368.280    0.000 layers.py:76(check)
               42528052  333.942    0.000  333.942    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1197894   10.998    0.000  288.499    0.000 layers.py:496(restart)
              297696448  232.144    0.000  286.475    0.000 tensor.py:906(grad)
              151886000  185.517    0.000  272.561    0.000 layers.py:110(isDone)
              859813428  177.501    0.000  250.518    0.000 enum.py:646(__hash__)
                4556577    7.121    0.000  242.912    0.000 loss.py:527(forward)
                4556577   18.261    0.000  235.790    0.000 functional.py:2898(mse_loss)
              151885900  154.649    0.000  229.205    0.000 layers.py:47(check)
                3037718   86.173    0.000  225.156    0.000 random.py:315(sample)
              151885900  137.358    0.000  224.859    0.000 layers.py:63(check)
             2234383501  222.664    0.000  222.664    0.000 layer.py:69(positions)
               13669731  212.151    0.000  212.151    0.000 {built-in method sum}
              370956682  202.408    0.000  202.408    0.000 layer.py:116(elements)
                1197894    6.107    0.000  191.892    0.000 level.py:8(__init__)
        1353148924/1353148921  138.465    0.000  180.293    0.000 {built-in method builtins.len}
                1197894   11.038    0.000  161.467    0.000 levels.py:122(generate)
                4556577  156.026    0.000  156.026    0.000 {built-in method torch._C._nn.mse_loss}
               24247174   17.446    0.000  154.822    0.000 flatten.py:39(forward)
                6048151  154.747    0.000  154.747    0.000 {built-in method multinomial}
                7594295   12.811    0.000  152.830    0.000 tensor.py:525(__rsub__)
                3593682   31.774    0.000  140.497    0.000 level.py:41(notUsed)
                4557332  138.647    0.000  138.647    0.000 {built-in method max}
                7594295  137.869    0.000  137.869    0.000 {built-in method rsub}
               24247174  137.375    0.000  137.375    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              159126698  121.656    0.000  121.656    0.000 {built-in method torch._C._get_tracing_state}
              176594758   84.142    0.000  114.703    0.000 layer.py:100(add)
                3037720  113.924    0.000  113.924    0.000 {built-in method nonzero}
              135038141   73.156    0.000  109.001    0.000 layer.py:96(remove)
                4556577  108.047    0.000  108.047    0.000 {built-in method gather}
                4556577   20.268    0.000  105.827    0.000 __init__.py:28(_make_grads)
                9113154   22.981    0.000  104.594    0.000 profiler.py:615(__enter__)
              825809725  101.139    0.000  101.139    0.000 layer.py:177(isBlocking)
                6308544  100.191    0.000  100.191    0.000 {method 'long' of 'torch._C._TensorBase' objects}
              155518381   65.664    0.000   97.153    0.000 random.py:250(_randbelow_with_getrandbits)
                6048755    7.348    0.000   96.075    0.000 functional.py:1553(softmax)
               10632017   95.437    0.000   95.437    0.000 {built-in method zeros}
                6048755   87.623    0.000   87.623    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              127295654   85.592    0.000   85.599    0.000 module.py:934(__getattr__)
                9113154   13.478    0.000   84.442    0.000 profiler.py:607(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9455325: <causal1_9x9_META_attempt2_0> in cluster <dcc> Done

Job <causal1_9x9_META_attempt2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 02:22:06 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 02:22:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 02:22:07 2021
Terminated at Wed Mar 24 13:17:42 2021
Results reported at Wed Mar 24 13:17:42 2021

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

    CPU time :                                   39216.00 sec.
    Max Memory :                                 6461 MB
    Average Memory :                             5029.04 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1731.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39360 sec.
    Turnaround time :                            39336 sec.

The output (if any) is above this job summary.

