
# Parameters

    Name :                      causal2_good-0
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     20.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1195 minutes.
    Hours used :                19 hours.

# Profiling


      58020868322 function calls (57809876503 primitive calls) in 71713.48 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71713.478 71713.478 {built-in method builtins.exec}
                      1    2.021    2.021 71713.478 71713.478 <string>:1(<module>)
                      1  185.166  185.166 71711.458 71711.458 main.py:43(teleport)
                7535662   29.383    0.000 21564.467    0.003 agent.py:27(learn)
                7535662  559.699    0.000 18218.954    0.002 learner.py:42(Qlearn)
                3767831   15.698    0.000 16893.863    0.004 game.py:27(step)
                3767831   21.412    0.000 16043.379    0.004 layers.py:475(step)
                3767831 7631.553    0.002 13825.933    0.004 replaybuffer.py:29(teleporter_save_data)
                3767831  399.912    0.000 13018.850    0.003 agent.py:52(_learn)
        237364981/26374173  961.439    0.000 8741.681    0.000 module.py:866(_call_impl)
                3767831  109.149    0.000 8500.759    0.002 agent.py:113(_learn)
                3767831 5723.443    0.002 8386.509    0.002 agent.py:84(interveen)
                3767831  286.710    0.000 8184.708    0.002 layers.py:18(step)
               18838511   57.133    0.000 8136.538    0.000 network.py:24(forward)
               18838511  264.289    0.000 7962.340    0.000 container.py:117(forward)
              376783100  467.537    0.000 7865.990    0.000 layer.py:76(move)
                3767832  395.414    0.000 7810.054    0.002 layers.py:446(update)
                7535662   67.013    0.000 7601.858    0.001 optimizer.py:84(wrapper)
                7535662   31.341    0.000 7291.991    0.001 grad_mode.py:24(decorate_context)
                7535662  210.002    0.000 7189.301    0.001 adam.py:55(step)
                7535662 1486.071    0.000 6733.338    0.001 _functional.py:53(adam)
                7535018  191.829    0.000 5434.056    0.001 agent.py:47(__call__)
              426086674 4980.270    0.000 4980.270    0.000 {built-in method clone}
                7535662   32.327    0.000 4588.200    0.001 tensor.py:195(backward)
                7535662   29.437    0.000 4554.645    0.001 __init__.py:68(backward)
                3767831 3195.740    0.001 4537.097    0.001 replaybuffer.py:23(sample_data)
              376783100  808.581    0.000 4474.085    0.000 layers.py:492(check)
                7535662 4358.422    0.001 4358.422    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               24215165  177.369    0.000 4046.632    0.000 layers.py:496(restart)
                3767831 2226.755    0.001 3365.736    0.001 agent.py:65(modify)
               37677022   82.801    0.000 2928.773    0.000 conv.py:398(forward)
               37677022   49.392    0.000 2808.891    0.000 conv.py:390(_conv_forward)
               37677022 2759.499    0.000 2759.499    0.000 {built-in method conv2d}
              376783100  556.746    0.000 2457.337    0.000 layers.py:486(isFree)
               24215165   83.595    0.000 2334.995    0.000 level.py:8(__init__)
               48979871  103.560    0.000 2265.750    0.000 linear.py:93(forward)
               30142656 1310.707    0.000 2189.652    0.000 layer.py:137(NoRock_update)
               48979871   39.860    0.000 2114.167    0.000 functional.py:1737(linear)
               48979871 2064.622    0.000 2064.622    0.000 {built-in method torch._C._nn.linear}
             2929264822 1529.624    0.000 1900.591    0.000 layer.py:73(isFree)
               24215165  135.690    0.000 1853.872    0.000 levels.py:151(generate)
                3767831   55.975    0.000 1735.584    0.000 agent.py:108(__call__)
               11302849   76.146    0.000 1636.158    0.000 agent.py:57(modify_board)
               48430330  362.590    0.000 1586.546    0.000 level.py:41(notUsed)
             6434395343 1049.609    0.000 1532.527    0.000 enum.py:646(__hash__)
              193721320  126.930    0.000 1473.781    0.000 layer.py:50(restart)
              135641916 1367.761    0.000 1367.761    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33909835 1345.348    0.000 1345.348    0.000 {built-in method cat}
              437389523 1316.008    0.000 1316.008    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               67818382   53.514    0.000 1269.272    0.000 activation.py:713(forward)
               67818382   54.371    0.000 1215.758    0.000 functional.py:1364(leaky_relu)
              135641916 1208.100    0.000 1208.100    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16158687 1198.820    0.000 1198.820    0.000 {built-in method tensor}
               67818382 1150.229    0.000 1150.229    0.000 {built-in method torch._C._nn.leaky_relu}
               24215265  567.266    0.000 1148.329    0.000 layers.py:33(reset)
                3767831   70.260    0.000 1074.611    0.000 replaybuffer.py:19(stacker)
                7535662  171.429    0.000 1072.292    0.000 optimizer.py:189(zero_grad)
               11302849 1051.112    0.000 1051.112    0.000 {built-in method torch._C._nn.one_hot}
              376783200  118.985    0.000 1034.449    0.000 {built-in method builtins.all}
              376783100  596.762    0.000  962.654    0.000 layers.py:302(check)
             1273295148  309.230    0.000  958.023    0.000 layers.py:452(<genexpr>)
              376783100  568.024    0.000  930.633    0.000 layers.py:261(check)
                7535662    8.620    0.000  929.757    0.000 game.py:23(board)
                3767831  461.482    0.000  762.218    0.000 collector.py:54(collect)
               67820958  748.399    0.000  748.399    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67820958  659.916    0.000  659.916    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              376783100  407.990    0.000  645.745    0.000 layers.py:328(check)
               67820958  624.734    0.000  624.734    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67820958  618.256    0.000  618.256    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               48430330   34.258    0.000  610.283    0.000 level.py:38(elementsIn)
              376783200  403.981    0.000  598.865    0.000 layers.py:110(isDone)
             1187959056  436.693    0.000  596.071    0.000 layer.py:100(add)
             2412022452  587.227    0.000  587.227    0.000 layer.py:116(elements)
              376783100  364.331    0.000  572.358    0.000 layers.py:287(check)
                7535018  207.880    0.000  567.764    0.000 exploration.py:53(softmaxer)
             6087187741  530.352    0.000  530.352    0.000 layer.py:69(positions)
               67820958  483.370    0.000  483.370    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6434422814  482.923    0.000  482.923    0.000 {built-in method builtins.hash}
              376783100  303.026    0.000  463.267    0.000 layers.py:47(check)
             2397301335  418.268    0.000  418.268    0.000 level.py:32(inverse)
              474746760  328.592    0.000  404.763    0.000 tensor.py:906(grad)
               48430330  194.127    0.000  378.331    0.000 level.py:39(<listcomp>)
                7535662   11.082    0.000  374.488    0.000 loss.py:527(forward)
                7535662   28.635    0.000  363.407    0.000 functional.py:2898(mse_loss)
               24215165  151.282    0.000  339.572    0.000 level.py:16(<dictcomp>)
               22606986  319.328    0.000  319.328    0.000 {built-in method sum}
        3361063296/3361063294  251.542    0.000  307.402    0.000 {built-in method builtins.len}
                3767831   94.859    0.000  259.552    0.000 random.py:315(sample)
              364640246  170.645    0.000  251.671    0.000 layer.py:96(remove)
             1380264412  249.117    0.000  249.117    0.000 enum.py:352(<genexpr>)
                7535662  238.077    0.000  238.077    0.000 {built-in method torch._C._nn.mse_loss}
             1985652386  224.960    0.000  224.960    0.000 layer.py:152(grid)
             3135708182  224.558    0.000  224.558    0.000 {method 'append' of 'list' objects}
               37677022   25.785    0.000  216.413    0.000 flatten.py:39(forward)
                3767831   16.532    0.000  208.787    0.000 exploration.py:47(epsilonGreedy)
               11303493   16.260    0.000  207.002    0.000 tensor.py:525(__rsub__)
                7536791  205.100    0.000  205.100    0.000 {built-in method max}
             2199984330  204.407    0.000  204.407    0.000 layer.py:177(isBlocking)
               48430330  124.701    0.000  197.694    0.000 {built-in method _functools.reduce}
               37677022  190.628    0.000  190.628    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9474223: <causal2_good_0> in cluster <dcc> Done

Job <causal2_good_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 27 17:45:03 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 17:45:04 2021
Terminated at Sun Mar 28 14:40:27 2021
Results reported at Sun Mar 28 14:40:27 2021

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

    CPU time :                                   71532.37 sec.
    Max Memory :                                 7793 MB
    Average Memory :                             5511.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8591.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71740 sec.
    Turnaround time :                            71724 sec.

The output (if any) is above this job summary.

