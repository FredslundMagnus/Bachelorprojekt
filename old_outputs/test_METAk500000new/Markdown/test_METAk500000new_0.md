
# Parameters

    Name :                      test_METAk500000new-0
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
    K :                         500000.0
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      5973610580 function calls (5904182945 primitive calls) in 14110.86 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14110.855 14110.855 {built-in method builtins.exec}
                      1    5.034    5.034 14110.855 14110.855 <string>:1(<module>)
                      1   59.202   59.202 14105.821 14105.821 main.py:14(metateleport)
                2338815    8.056    0.000 5836.576    0.002 agent.py:27(learn)
                2338815  146.926    0.000 4713.188    0.002 learner.py:42(Qlearn)
                1559210   55.475    0.000 4368.361    0.003 agent.py:51(_learn)
                1559210 2360.314    0.002 2904.450    0.002 replaybuffer.py:23(sample_data)
        77810114/8384178  324.820    0.000 2577.631    0.000 module.py:866(_call_impl)
                6045363   17.216    0.000 2401.754    0.000 network.py:24(forward)
                6045363   78.103    0.000 2344.814    0.000 container.py:117(forward)
                2926943   67.924    0.000 1886.954    0.001 agent.py:46(__call__)
                2338815   19.623    0.000 1842.443    0.001 optimizer.py:84(wrapper)
                2338815   10.819    0.000 1752.271    0.001 grad_mode.py:24(decorate_context)
                2338815   71.481    0.000 1719.062    0.001 adam.py:55(step)
                2338815  358.502    0.000 1562.595    0.001 _functional.py:53(adam)
                 779605    3.620    0.000 1522.284    0.002 game.py:27(step)
                 779605   22.808    0.000 1454.354    0.002 agent.py:110(_learn)
                 779605    4.783    0.000 1396.639    0.002 layers.py:475(step)
                1559210  388.839    0.000 1262.872    0.001 agent.py:81(interveen)
                2338815    9.635    0.000 1205.468    0.001 tensor.py:195(backward)
                2338815    9.756    0.000 1195.447    0.001 __init__.py:68(backward)
                2338815 1138.248    0.000 1138.248    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 779605  674.095    0.001 1058.845    0.001 agent.py:114(metamodify)
               12090726   29.958    0.000  867.642    0.000 conv.py:398(forward)
                1559210  481.835    0.000  852.785    0.001 replaybuffer.py:27(teleporter_save_data)
               12090726   18.187    0.000  824.143    0.000 conv.py:390(_conv_forward)
               12090726  805.956    0.000  805.956    0.000 {built-in method conv2d}
                 779605   69.358    0.000  721.545    0.001 layers.py:18(step)
                 779606   87.277    0.000  663.296    0.001 layers.py:446(update)
               16576879   35.917    0.000  658.176    0.000 linear.py:93(forward)
               77960500   92.105    0.000  643.814    0.000 layer.py:76(move)
               16576879   13.483    0.000  604.707    0.000 functional.py:1737(linear)
               16576879  587.894    0.000  587.894    0.000 {built-in method torch._C._nn.linear}
                4486153   39.205    0.000  574.296    0.000 agent.py:55(modify_board)
               13841413  502.037    0.000  502.037    0.000 {built-in method cat}
                1559210   36.319    0.000  424.842    0.000 replaybuffer.py:19(stacker)
                4486153  366.954    0.000  366.954    0.000 {built-in method torch._C._nn.one_hot}
               77960500   55.491    0.000  366.822    0.000 layers.py:486(isFree)
               22622242   18.399    0.000  345.926    0.000 activation.py:713(forward)
                 779605   12.702    0.000  339.414    0.000 agent.py:105(__call__)
               33524284  331.724    0.000  331.724    0.000 {built-in method clone}
               22622242   18.930    0.000  327.527    0.000 functional.py:1364(leaky_relu)
              224293362  272.372    0.000  311.331    0.000 layer.py:73(isFree)
               22622242  304.531    0.000  304.531    0.000 {built-in method torch._C._nn.leaky_relu}
               43657880  300.391    0.000  300.391    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2338815   48.586    0.000  273.821    0.000 optimizer.py:189(zero_grad)
               43657880  269.449    0.000  269.449    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2338818  135.197    0.000  221.826    0.000 layer.py:137(NoRock_update)
               77960600   22.572    0.000  219.687    0.000 {built-in method builtins.all}
                4183113  209.502    0.000  209.502    0.000 {built-in method tensor}
              234128225   57.982    0.000  206.473    0.000 layers.py:452(<genexpr>)
                2926943   70.948    0.000  188.051    0.000 exploration.py:53(softmaxer)
               21828940  181.650    0.000  181.650    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 779605   95.059    0.000  161.376    0.000 collector.py:54(collect)
                2338815    2.556    0.000  160.751    0.000 game.py:23(board)
               21828940  155.118    0.000  155.118    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               21828940  147.586    0.000  147.586    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21828940  144.135    0.000  144.135    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               77960600   95.078    0.000  141.671    0.000 layers.py:110(isDone)
              152802664  108.003    0.000  133.626    0.000 tensor.py:906(grad)
                1559210   44.198    0.000  116.003    0.000 random.py:315(sample)
               21828940  105.065    0.000  105.065    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2338815    3.425    0.000  103.650    0.000 loss.py:527(forward)
                 430570    3.745    0.000  102.157    0.000 layers.py:496(restart)
                2338815    9.624    0.000  100.225    0.000 functional.py:2898(mse_loss)
               77960500   64.719    0.000   83.868    0.000 layers.py:492(check)
               37230832   82.319    0.000   82.319    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        588234808/588234805   57.831    0.000   76.131    0.000 {built-in method builtins.len}
                7016445   75.309    0.000   75.309    0.000 {built-in method sum}
                 430570    2.200    0.000   69.602    0.000 level.py:8(__init__)
                2338815   61.803    0.000   61.803    0.000 {built-in method torch._C._nn.mse_loss}
                3898025    5.239    0.000   58.786    0.000 tensor.py:525(__rsub__)
                2926943   58.673    0.000   58.673    0.000 {built-in method multinomial}
               12090726    8.758    0.000   58.526    0.000 flatten.py:39(forward)
                 430570    3.857    0.000   58.208    0.000 levels.py:122(generate)
                2339184   55.039    0.000   55.039    0.000 {built-in method max}
               87809011   39.479    0.000   54.470    0.000 layer.py:100(add)
               73166431   36.836    0.000   54.318    0.000 layer.py:96(remove)
              179958352   53.425    0.000   53.425    0.000 layer.py:116(elements)
                3898025   52.589    0.000   52.589    0.000 {built-in method rsub}
               79275186   34.422    0.000   50.933    0.000 random.py:250(_randbelow_with_getrandbits)
                1291710   12.080    0.000   50.656    0.000 level.py:41(notUsed)
                 779605    3.799    0.000   50.196    0.000 exploration.py:47(epsilonGreedy)
               12090726   49.768    0.000   49.768    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1559212   47.488    0.000   47.488    0.000 {built-in method nonzero}
                2338815    9.662    0.000   45.335    0.000 __init__.py:28(_make_grads)
               79369908   45.141    0.000   45.141    0.000 {built-in method torch._C._get_tracing_state}
                2338815   44.159    0.000   44.159    0.000 {built-in method gather}
              463153276   43.749    0.000   43.749    0.000 layer.py:69(positions)
                4677630   10.255    0.000   43.701    0.000 profiler.py:615(__enter__)
               63386730   42.033    0.000   42.037    0.000 module.py:934(__getattr__)
                5457239   40.165    0.000   40.165    0.000 {built-in method zeros}
                3399198   40.123    0.000   40.123    0.000 {method 'long' of 'torch._C._TensorBase' objects}
                4677630    6.771    0.000   37.275    0.000 profiler.py:607(__init__)
                2927235    3.211    0.000   35.151    0.000 functional.py:1553(softmax)
              114989623   24.221    0.000   35.042    0.000 enum.py:646(__hash__)
                4677630   33.446    0.000   33.446    0.000 {built-in method torch._ops.profiler._record_function_enter}
                2338815   33.203    0.000   33.203    0.000 {built-in method ones_like}
                2927235   31.480    0.000   31.480    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              361156605   31.192    0.000   31.192    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9457752: <test_METAk500000new_0> in cluster <dcc> Done

Job <test_METAk500000new_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:29:15 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 17:29:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 17:29:16 2021
Terminated at Wed Mar 24 21:24:31 2021
Results reported at Wed Mar 24 21:24:31 2021

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

    CPU time :                                   14076.70 sec.
    Max Memory :                                 5089 MB
    Average Memory :                             4387.26 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3103.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14132 sec.
    Turnaround time :                            14116 sec.

The output (if any) is above this job summary.

