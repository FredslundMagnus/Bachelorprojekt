
# Parameters

    Name :                      causal1_9x9_META_attempt2_highK-0
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
    K :                         500000.0
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


      21094893713 function calls (20913638422 primitive calls) in 39309.84 seconds

##    Ordered by: cumulative time
   List reduced from 468 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39309.840 39309.840 {built-in method builtins.exec}
                      1    5.098    5.098 39309.840 39309.840 <string>:1(<module>)
                      1  147.979  147.979 39304.742 39304.742 main.py:14(metateleport)
                5923242   20.251    0.000 14324.797    0.002 agent.py:27(learn)
                5923242  352.425    0.000 11563.711    0.002 learner.py:42(Qlearn)
                3948828  138.918    0.000 10718.347    0.003 agent.py:51(_learn)
                3948828 5338.606    0.001 6627.456    0.002 replaybuffer.py:23(sample_data)
        202939438/21685846  796.479    0.000 6476.986    0.000 module.py:866(_call_impl)
               15762604   46.400    0.000 6048.285    0.000 network.py:24(forward)
                1974414    8.561    0.000 5953.859    0.003 game.py:27(step)
               15762604  197.760    0.000 5900.178    0.000 container.py:117(forward)
                1974414   11.856    0.000 5585.181    0.003 layers.py:475(step)
                7864948  189.677    0.000 4895.937    0.001 agent.py:46(__call__)
                5923242   50.129    0.000 4517.675    0.001 optimizer.py:84(wrapper)
                5923242   25.351    0.000 4298.406    0.001 grad_mode.py:24(decorate_context)
                5923242  168.299    0.000 4219.149    0.001 adam.py:55(step)
                3948828 1703.775    0.000 4119.680    0.001 agent.py:81(interveen)
                3948828 2248.569    0.001 3969.208    0.001 replaybuffer.py:27(teleporter_save_data)
                5923242  885.367    0.000 3851.955    0.001 _functional.py:53(adam)
                1974414   59.821    0.000 3571.810    0.002 agent.py:146(_learn)
                1974414  169.585    0.000 3451.286    0.002 layers.py:18(step)
              197441400  431.958    0.000 3264.784    0.000 layer.py:76(move)
                5923242   23.105    0.000 2991.489    0.001 tensor.py:195(backward)
                5923242   24.750    0.000 2967.561    0.001 __init__.py:68(backward)
                5923242 2829.500    0.000 2829.500    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1974414 1657.770    0.001 2596.399    0.001 agent.py:101(metamodify)
               31525208   72.007    0.000 2170.777    0.000 conv.py:398(forward)
                1974415  213.533    0.000 2106.112    0.001 layers.py:446(update)
               31525208   40.681    0.000 2066.249    0.000 conv.py:390(_conv_forward)
               31525208 2025.567    0.000 2025.567    0.000 {built-in method conv2d}
               43338984   89.992    0.000 1680.886    0.000 linear.py:93(forward)
               43338984   36.502    0.000 1547.551    0.000 functional.py:1737(linear)
               43338984 1503.023    0.000 1503.023    0.000 {built-in method torch._C._nn.linear}
              159494646 1480.263    0.000 1480.263    0.000 {built-in method clone}
               11813776   98.129    0.000 1461.670    0.000 agent.py:55(modify_board)
              197441400  345.734    0.000 1374.667    0.000 layers.py:492(check)
               35506744 1236.093    0.000 1236.093    0.000 {built-in method cat}
              197441400  228.021    0.000 1149.953    0.000 layers.py:486(isFree)
                3948828   70.650    0.000 1008.980    0.000 replaybuffer.py:19(stacker)
               11813776  927.871    0.000  927.871    0.000 {built-in method torch._C._nn.one_hot}
             1068236845  774.768    0.000  921.933    0.000 layer.py:73(isFree)
               11846490  552.361    0.000  913.466    0.000 layer.py:121(update)
               59101588   48.403    0.000  881.425    0.000 activation.py:713(forward)
               59101588   48.969    0.000  833.021    0.000 functional.py:1364(leaky_relu)
                1974414   30.434    0.000  801.669    0.000 agent.py:141(__call__)
               59101588  773.994    0.000  773.994    0.000 {built-in method torch._C._nn.leaky_relu}
              110567184  748.071    0.000  748.071    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               10282114  671.850    0.000  671.850    0.000 {built-in method tensor}
                5923242  116.614    0.000  669.948    0.000 optimizer.py:189(zero_grad)
              110567184  667.089    0.000  667.089    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5923242    6.175    0.000  562.518    0.000 game.py:23(board)
              197441500   63.955    0.000  525.137    0.000 {built-in method builtins.all}
                7864948  182.453    0.000  485.892    0.000 exploration.py:53(softmaxer)
              595437929  142.273    0.000  483.787    0.000 layers.py:452(<genexpr>)
               55283592  448.170    0.000  448.170    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              197441400  318.295    0.000  445.053    0.000 layers.py:76(check)
                1974414  235.311    0.000  398.321    0.000 collector.py:54(collect)
               55283592  382.481    0.000  382.481    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1667436   14.379    0.000  376.109    0.000 layers.py:496(restart)
               55283592  354.389    0.000  354.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               55283592  353.208    0.000  353.208    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              169334008  340.689    0.000  340.689    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              197441500  218.969    0.000  322.969    0.000 layers.py:110(isDone)
              386985228  251.208    0.000  311.888    0.000 tensor.py:906(grad)
             1124491128  211.766    0.000  304.217    0.000 enum.py:646(__hash__)
              197441400  188.267    0.000  282.763    0.000 layers.py:47(check)
                3948828  104.076    0.000  272.104    0.000 random.py:315(sample)
               55283592  269.445    0.000  269.445    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2899102669  254.858    0.000  254.858    0.000 layer.py:69(positions)
              197441400  165.668    0.000  252.216    0.000 layers.py:63(check)
                1667436    7.607    0.000  250.069    0.000 level.py:8(__init__)
                5923242    7.579    0.000  248.159    0.000 loss.py:527(forward)
                5923242   22.026    0.000  240.580    0.000 functional.py:2898(mse_loss)
              487775124  233.720    0.000  233.720    0.000 layer.py:116(elements)
                1667436   13.692    0.000  212.170    0.000 levels.py:122(generate)
        1761399191/1761399188  154.218    0.000  200.707    0.000 {built-in method builtins.len}
               17769726  186.014    0.000  186.014    0.000 {built-in method sum}
                5002308   41.675    0.000  185.367    0.000 level.py:41(notUsed)
                7864948  153.845    0.000  153.845    0.000 {built-in method multinomial}
                5923242  147.650    0.000  147.650    0.000 {built-in method torch._C._nn.mse_loss}
               31525208   22.194    0.000  145.655    0.000 flatten.py:39(forward)
                9872070   13.027    0.000  142.905    0.000 tensor.py:525(__rsub__)
              232356368  102.645    0.000  137.264    0.000 layer.py:100(add)
                5924224  135.197    0.000  135.197    0.000 {built-in method max}
              174520601   88.453    0.000  130.040    0.000 layer.py:96(remove)
                9872070  127.466    0.000  127.466    0.000 {built-in method rsub}
               31525208  123.460    0.000  123.460    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              202493940   81.837    0.000  120.350    0.000 random.py:250(_randbelow_with_getrandbits)
              206889836  114.531    0.000  114.531    0.000 {built-in method torch._C._get_tracing_state}
                3948830  113.313    0.000  113.313    0.000 {built-in method nonzero}
                5923242   22.904    0.000  108.186    0.000 __init__.py:28(_make_grads)
               10004616    8.830    0.000  108.065    0.000 layer.py:50(restart)
               11846484   24.524    0.000  105.377    0.000 profiler.py:615(__enter__)
              165506025  104.844    0.000  104.853    0.000 module.py:934(__getattr__)
                5923242  103.955    0.000  103.955    0.000 {built-in method gather}
             1068236845  100.870    0.000  100.870    0.000 layer.py:177(isBlocking)
                8296670   97.762    0.000   97.762    0.000 {method 'long' of 'torch._C._TensorBase' objects}
               13820902   97.502    0.000   97.502    0.000 {built-in method zeros}
             1124513899   92.455    0.000   92.455    0.000 {built-in method builtins.hash}
                1974414    8.429    0.000   90.287    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 9455327: <causal1_9x9_META_attempt2_highK_0> in cluster <dcc> Done

Job <causal1_9x9_META_attempt2_highK_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 02:22:07 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 02:29:56 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 02:29:56 2021
Terminated at Wed Mar 24 13:25:12 2021
Results reported at Wed Mar 24 13:25:12 2021

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

    CPU time :                                   39203.12 sec.
    Max Memory :                                 7302 MB
    Average Memory :                             5452.62 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               890.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39316 sec.
    Turnaround time :                            39785 sec.

The output (if any) is above this job summary.

