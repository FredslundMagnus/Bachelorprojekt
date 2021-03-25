
# Parameters

    Name :                      test_METAk1000000new-0
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
    K :                         1000000.0
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


      6469765214 function calls (6395129339 primitive calls) in 14114.63 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14114.632 14114.632 {built-in method builtins.exec}
                      1    5.017    5.017 14114.632 14114.632 <string>:1(<module>)
                      1   57.768   57.768 14109.615 14109.615 main.py:14(metateleport)
                2498232    8.154    0.000 5702.224    0.002 agent.py:27(learn)
                2498232  140.828    0.000 4603.327    0.002 learner.py:42(Qlearn)
                1665488   53.946    0.000 4268.445    0.003 agent.py:51(_learn)
                1665488 2492.190    0.001 3026.341    0.002 replaybuffer.py:23(sample_data)
        83629504/8995328  315.768    0.000 2522.309    0.000 module.py:866(_call_impl)
                6497096   17.049    0.000 2351.922    0.000 network.py:24(forward)
                6497096   76.719    0.000 2295.187    0.000 container.py:117(forward)
                3166120   67.827    0.000 1866.957    0.001 agent.py:46(__call__)
                2498232   19.487    0.000 1799.345    0.001 optimizer.py:84(wrapper)
                2498232   10.189    0.000 1712.989    0.001 grad_mode.py:24(decorate_context)
                2498232   68.094    0.000 1680.579    0.001 adam.py:55(step)
                2498232  344.988    0.000 1532.678    0.001 _functional.py:53(adam)
                 832744    3.435    0.000 1486.605    0.002 game.py:27(step)
                 832744   22.579    0.000 1420.621    0.002 agent.py:110(_learn)
                 832744    4.983    0.000 1362.087    0.002 layers.py:475(step)
                1665488  404.012    0.000 1279.347    0.001 agent.py:81(interveen)
                2498232    8.880    0.000 1187.879    0.000 tensor.py:195(backward)
                2498232    9.165    0.000 1178.659    0.000 __init__.py:68(backward)
                2498232 1123.962    0.000 1123.962    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 832744  671.416    0.001 1050.757    0.001 agent.py:114(metamodify)
                1665488  503.294    0.000  885.969    0.001 replaybuffer.py:27(teleporter_save_data)
               12994192   27.946    0.000  846.439    0.000 conv.py:398(forward)
               12994192   16.506    0.000  806.026    0.000 conv.py:390(_conv_forward)
               12994192  789.520    0.000  789.520    0.000 {built-in method conv2d}
                 832744   65.715    0.000  683.123    0.001 layers.py:18(step)
                 832745   81.239    0.000  666.724    0.001 layers.py:446(update)
               17825800   33.967    0.000  647.404    0.000 linear.py:93(forward)
               83274400   84.989    0.000  610.073    0.000 layer.py:76(move)
               17825800   13.176    0.000  596.422    0.000 functional.py:1737(linear)
               17825800  579.988    0.000  579.988    0.000 {built-in method torch._C._nn.linear}
                4831608   38.638    0.000  576.509    0.000 agent.py:55(modify_board)
               14824536  496.958    0.000  496.958    0.000 {built-in method cat}
                1665488   36.200    0.000  418.789    0.000 replaybuffer.py:19(stacker)
                4831608  369.219    0.000  369.219    0.000 {built-in method torch._C._nn.one_hot}
               83274400   52.612    0.000  350.449    0.000 layers.py:486(isFree)
                 832744   12.392    0.000  348.270    0.000 agent.py:105(__call__)
               24322896   22.029    0.000  344.415    0.000 activation.py:713(forward)
               38074480  340.927    0.000  340.927    0.000 {built-in method clone}
               24322896   18.311    0.000  322.386    0.000 functional.py:1364(leaky_relu)
               24322896  300.289    0.000  300.289    0.000 {built-in method torch._C._nn.leaky_relu}
              237068434  262.910    0.000  297.837    0.000 layer.py:73(isFree)
               46633664  297.626    0.000  297.626    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46633664  267.393    0.000  267.393    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2498232   45.761    0.000  264.411    0.000 optimizer.py:189(zero_grad)
                2498235  133.907    0.000  222.687    0.000 layer.py:137(NoRock_update)
                4654195  219.861    0.000  219.861    0.000 {built-in method tensor}
               83274500   21.468    0.000  209.355    0.000 {built-in method builtins.all}
              250284518   55.890    0.000  196.811    0.000 layers.py:452(<genexpr>)
                3166120   68.262    0.000  183.451    0.000 exploration.py:53(softmaxer)
               23316832  174.661    0.000  174.661    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2498232    2.403    0.000  165.665    0.000 game.py:23(board)
                 832744   92.452    0.000  157.073    0.000 collector.py:54(collect)
               23316832  155.365    0.000  155.365    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               23316832  143.786    0.000  143.786    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               23316832  143.525    0.000  143.525    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               83274500   90.718    0.000  134.464    0.000 layers.py:110(isDone)
              163217908   99.979    0.000  124.042    0.000 tensor.py:906(grad)
                 578347    4.514    0.000  121.976    0.000 layers.py:496(restart)
                1665488   42.646    0.000  112.214    0.000 random.py:315(sample)
               23316832  106.342    0.000  106.342    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2498232    3.098    0.000   99.892    0.000 loss.py:527(forward)
                2498232    8.520    0.000   96.794    0.000 functional.py:2898(mse_loss)
               42073344   83.612    0.000   83.612    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 578347    2.760    0.000   82.948    0.000 level.py:8(__init__)
               83274400   60.305    0.000   78.015    0.000 layers.py:492(check)
                7494696   74.269    0.000   74.269    0.000 {built-in method sum}
        630867242/630867239   55.661    0.000   73.222    0.000 {built-in method builtins.len}
                 578347    4.602    0.000   69.300    0.000 levels.py:122(generate)
                 832744    4.459    0.000   66.694    0.000 exploration.py:47(epsilonGreedy)
                1735041   14.613    0.000   60.369    0.000 level.py:41(notUsed)
                2498232   59.944    0.000   59.944    0.000 {built-in method torch._C._nn.mse_loss}
                3166120   58.712    0.000   58.712    0.000 {built-in method multinomial}
                4163720    5.138    0.000   57.109    0.000 tensor.py:525(__rsub__)
              197572893   56.612    0.000   56.612    0.000 layer.py:116(elements)
               12994192    8.366    0.000   56.134    0.000 flatten.py:39(forward)
               96564015   39.197    0.000   54.205    0.000 layer.py:100(add)
                2498631   53.930    0.000   53.930    0.000 {built-in method max}
               76897017   35.095    0.000   51.912    0.000 layer.py:96(remove)
                4163720   51.050    0.000   51.050    0.000 {built-in method rsub}
               85033221   32.887    0.000   49.122    0.000 random.py:250(_randbelow_with_getrandbits)
               12994192   47.767    0.000   47.767    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1665490   46.628    0.000   46.628    0.000 {built-in method nonzero}
                2498232    9.027    0.000   43.527    0.000 __init__.py:28(_make_grads)
               85295624   43.057    0.000   43.057    0.000 {built-in method torch._C._get_tracing_state}
                2498232   42.426    0.000   42.426    0.000 {built-in method gather}
                4996464    8.760    0.000   41.424    0.000 profiler.py:615(__enter__)
               68143681   40.609    0.000   40.613    0.000 module.py:934(__getattr__)
              493386546   40.172    0.000   40.172    0.000 layer.py:69(positions)
                3816805   39.954    0.000   39.954    0.000 {method 'long' of 'torch._C._TensorBase' objects}
                5829212   38.583    0.000   38.583    0.000 {built-in method zeros}
                 485827   16.377    0.000   35.662    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              133012345   24.673    0.000   35.535    0.000 enum.py:646(__hash__)
                4996464    5.994    0.000   35.231    0.000 profiler.py:607(__init__)
                3166436    3.034    0.000   34.024    0.000 functional.py:1553(softmax)
                1735041    1.968    0.000   33.769    0.000 layer.py:50(restart)
                4996464   32.663    0.000   32.663    0.000 {built-in method torch._ops.profiler._record_function_enter}
                2498232   32.583    0.000   32.583    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9457753: <test_METAk1000000new_0> in cluster <dcc> Done

Job <test_METAk1000000new_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:29:15 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 18:05:00 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 18:05:00 2021
Terminated at Wed Mar 24 22:00:21 2021
Results reported at Wed Mar 24 22:00:21 2021

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

    CPU time :                                   14076.40 sec.
    Max Memory :                                 5183 MB
    Average Memory :                             4445.01 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3009.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14123 sec.
    Turnaround time :                            16266 sec.

The output (if any) is above this job summary.

