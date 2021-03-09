
# Parameters

    Name :                      9x9_K_500000_epsilon_cap_0.1-0
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
    K :                         500000.0
    Epsilon cap :               0.1
    Softmax cap :               0.03
    Gamma :                     0.98
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


      25520009666 function calls (25386010055 primitive calls) in 35685.09 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35704.193 35704.193 {built-in method builtins.exec}
                      1    0.775    0.775 35704.193 35704.193 <string>:1(<module>)
                      1  129.707  129.707 35703.418 35703.418 main.py:10(teleport)
                4786056   18.848    0.000 13427.348    0.003 agent.py:26(learn)
                4786056  319.956    0.000 11463.423    0.002 learner.py:42(Qlearn)
                2393028   11.558    0.000 8977.418    0.004 game.py:21(step)
                2393028   15.693    0.000 8426.100    0.004 layers.py:212(step)
                2393028   78.720    0.000 8015.913    0.003 agent.py:50(_learn)
        150748882/16750282  604.525    0.000 5649.315    0.000 module.py:715(_call_impl)
                2393028  217.492    0.000 5461.297    0.002 layers.py:17(step)
                2393028   68.319    0.000 5382.907    0.002 agent.py:101(_learn)
               11964226   29.081    0.000 5264.023    0.000 network.py:24(forward)
              239302800  254.377    0.000 5221.661    0.000 layer.py:66(move)
               11964226  138.456    0.000 5153.744    0.000 container.py:115(forward)
                4786056   31.613    0.000 4541.123    0.001 grad_mode.py:23(decorate_context)
                4786056  163.874    0.000 4451.257    0.001 adam.py:55(step)
                4786056  803.796    0.000 3627.299    0.001 functional.py:53(adam)
                2393028 1789.245    0.001 3507.754    0.001 agent.py:77(interveen)
                4785142  117.764    0.000 3480.742    0.001 agent.py:45(__call__)
                2393028 1926.122    0.001 3391.980    0.001 replaybuffer.py:27(teleporter_save_data)
                2393029  229.252    0.000 2925.473    0.001 layers.py:192(update)
              239302800  527.177    0.000 2745.618    0.000 layers.py:229(check)
                4786056   27.805    0.000 2733.179    0.001 tensor.py:181(backward)
                4786056   18.100    0.000 2705.374    0.001 __init__.py:68(backward)
                4786056 2577.185    0.001 2577.185    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2393028 1450.501    0.001 2534.711    0.001 replaybuffer.py:23(sample_data)
              239302800  331.830    0.000 1963.430    0.000 layers.py:223(isFree)
                2393028  904.347    0.000 1911.307    0.001 agent.py:59(modify)
               23928452   40.618    0.000 1898.803    0.000 conv.py:422(forward)
               23928452   51.047    0.000 1839.548    0.000 conv.py:414(_conv_forward)
               23928452 1779.755    0.000 1779.755    0.000 {built-in method conv2d}
               31106622   69.235    0.000 1650.405    0.000 linear.py:92(forward)
             1452728280 1405.540    0.000 1631.601    0.000 layer.py:63(isFree)
               31106622  114.554    0.000 1545.656    0.000 functional.py:1669(linear)
              109349276 1186.294    0.000 1186.294    0.000 {built-in method clone}
              301521582  709.287    0.000 1175.984    0.000 tensor.py:933(grad)
               19144232  411.966    0.000 1127.197    0.000 layer.py:90(update)
                2393028   35.212    0.000 1097.415    0.000 agent.py:96(__call__)
               31106622 1093.150    0.000 1093.150    0.000 {built-in method addmm}
               19143310 1075.007    0.000 1075.007    0.000 {built-in method cat}
                7178170   47.444    0.000 1056.920    0.000 agent.py:54(modify_board)
                4786056   97.099    0.000 1018.530    0.000 optimizer.py:167(zero_grad)
              239302800  620.940    0.000  985.096    0.000 layers.py:124(check)
                2393028   42.901    0.000  896.197    0.000 replaybuffer.py:19(stacker)
                1214049   15.351    0.000  836.819    0.001 layers.py:233(restart)
               10022906  764.934    0.000  764.934    0.000 {built-in method tensor}
               86149008  734.839    0.000  734.839    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               43070848   36.339    0.000  711.330    0.000 activation.py:713(forward)
                1214049    3.395    0.000  706.663    0.001 levels.py:8(__init__)
                1214049   12.265    0.000  703.268    0.001 level.py:8(__init__)
                7178170  684.999    0.000  684.999    0.000 {built-in method torch._C._nn.one_hot}
               43070848   54.329    0.000  674.991    0.000 functional.py:1292(leaky_relu)
              248876922   73.164    0.000  674.290    0.000 {built-in method builtins.all}
                1657215  106.351    0.000  671.276    0.000 levels.py:11(generate)
              724920474  176.462    0.000  622.862    0.000 layers.py:197(<genexpr>)
              385276342  207.080    0.000  616.198    0.000 overrides.py:1070(has_torch_function)
               43070848  615.103    0.000  615.103    0.000 {built-in method torch._C._nn.leaky_relu}
                4786056    8.723    0.000  611.002    0.000 game.py:17(board)
               86149008  604.608    0.000  604.608    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              641637211  575.240    0.000  575.240    0.000 layer.py:85(elements)
             2036262187  387.724    0.000  550.007    0.000 enum.py:646(__hash__)
              239302800  290.538    0.000  445.785    0.000 layers.py:95(check)
               43074504  428.673    0.000  428.673    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2393028  249.115    0.000  428.116    0.000 collector.py:37(collect)
              239302900  292.729    0.000  423.923    0.000 layers.py:65(isDone)
               43074504  394.106    0.000  394.106    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              425955077  157.084    0.000  388.057    0.000 {built-in method builtins.any}
              239302800  262.436    0.000  371.466    0.000 layers.py:50(check)
                4785142  129.776    0.000  363.189    0.000 exploration.py:53(softmaxer)
               43074504  349.874    0.000  349.874    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              116527446  345.166    0.000  345.166    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3683174770  338.214    0.000  338.214    0.000 layer.py:59(positions)
              239302800  223.144    0.000  337.112    0.000 layers.py:77(check)
               43074504  299.528    0.000  299.528    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9574022   43.731    0.000  273.941    0.000 tensor.py:21(wrapped)
                4786056    7.290    0.000  253.053    0.000 loss.py:445(forward)
                4786056   30.722    0.000  245.763    0.000 functional.py:2637(mse_loss)
               43074504  236.346    0.000  236.346    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1657215  121.445    0.000  227.953    0.000 levels.py:76(RFS)
              811232850  184.016    0.000  227.514    0.000 overrides.py:1083(<genexpr>)
                6921507   85.640    0.000  219.247    0.000 random.py:315(sample)
               31106622  199.775    0.000  199.775    0.000 {method 't' of 'torch._C._TensorBase' objects}
              302261246  140.785    0.000  192.635    0.000 layer.py:76(add)
              232562390  131.424    0.000  189.674    0.000 layer.py:72(remove)
               14358168  173.665    0.000  173.665    0.000 {built-in method sum}
             2036279794  162.287    0.000  162.287    0.000 {built-in method builtins.hash}
                3642147   22.489    0.000  160.553    0.000 level.py:41(notUsed)
                7179084   32.922    0.000  147.577    0.000 tensor.py:506(__rsub__)
             1275743040  145.649    0.000  145.649    0.000 layer.py:125(isBlocking)
                4786056  139.824    0.000  139.824    0.000 {built-in method torch._C._nn.mse_loss}
                7179084  135.064    0.000  135.064    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               23928452   17.509    0.000  129.212    0.000 flatten.py:39(forward)
                4786773  126.362    0.000  126.362    0.000 {built-in method max}
        415316969/415316967   60.761    0.000  125.693    0.000 {built-in method builtins.len}
               43074594   53.545    0.000  119.886    0.000 tensor.py:596(__hash__)
                4785142  116.015    0.000  116.015    0.000 {built-in method multinomial}
                7179084  114.655    0.000  114.655    0.000 {built-in method rsub}
                2393028   12.699    0.000  114.358    0.000 exploration.py:47(epsilonGreedy)
              121326711  112.346    0.000  112.346    0.000 level.py:32(inverse)
               23928452  111.703    0.000  111.703    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9395474: <9x9_K_500000_epsilon_cap_0.1_0> in cluster <dcc> Done

Job <9x9_K_500000_epsilon_cap_0.1_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Tue Mar  9 00:59:03 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar  9 01:04:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:04:35 2021
Terminated at Tue Mar  9 11:00:12 2021
Results reported at Tue Mar  9 11:00:12 2021

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

    CPU time :                                   35618.94 sec.
    Max Memory :                                 2385 MB
    Average Memory :                             2374.61 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5807.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35726 sec.
    Turnaround time :                            36069 sec.

The output (if any) is above this job summary.

