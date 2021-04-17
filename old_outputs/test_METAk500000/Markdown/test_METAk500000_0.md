
# Parameters

    Name :                      test_METAk500000-0
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


      5558216797 function calls (5493944890 primitive calls) in 14117.31 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14117.313 14117.313 {built-in method builtins.exec}
                      1    5.696    5.696 14117.313 14117.313 <string>:1(<module>)
                      1   63.074   63.074 14111.617 14111.617 main.py:14(metateleport)
                2159202    8.142    0.000 5444.265    0.003 agent.py:27(learn)
                2159202  134.687    0.000 4371.816    0.002 learner.py:42(Qlearn)
                1439468   52.180    0.000 4073.354    0.003 agent.py:51(_learn)
                1439468 3045.502    0.002 3560.048    0.002 replaybuffer.py:23(sample_data)
        72025172/7754964  306.965    0.000 2397.000    0.000 module.py:866(_call_impl)
                5595762   15.730    0.000 2227.830    0.000 network.py:24(forward)
                5595762   74.635    0.000 2172.701    0.000 container.py:117(forward)
                2716826   72.013    0.000 1781.239    0.001 agent.py:46(__call__)
                2159202   20.751    0.000 1685.976    0.001 optimizer.py:84(wrapper)
                2159202   11.521    0.000 1600.058    0.001 grad_mode.py:24(decorate_context)
                2159202   71.015    0.000 1564.802    0.001 adam.py:55(step)
                 719734    3.964    0.000 1453.785    0.002 game.py:27(step)
                2159202  326.133    0.000 1416.855    0.001 _functional.py:53(adam)
                 719734   21.892    0.000 1355.209    0.002 agent.py:110(_learn)
                 719734    4.806    0.000 1333.981    0.002 layers.py:475(step)
                1439468  387.847    0.000 1203.253    0.001 agent.py:81(interveen)
                2159202    9.401    0.000 1146.103    0.001 tensor.py:195(backward)
                2159202    9.998    0.000 1136.390    0.001 __init__.py:68(backward)
                2159202 1082.279    0.001 1082.279    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 719734  636.013    0.001  992.066    0.001 agent.py:114(metamodify)
                1439468  482.418    0.000  821.672    0.001 replaybuffer.py:27(teleporter_save_data)
               11191524   25.658    0.000  800.632    0.000 conv.py:398(forward)
               11191524   16.574    0.000  761.911    0.000 conv.py:390(_conv_forward)
               11191524  745.338    0.000  745.338    0.000 {built-in method conv2d}
                 719734   66.924    0.000  692.417    0.001 layers.py:18(step)
                 719735   79.039    0.000  629.076    0.001 layers.py:446(update)
               71973400   83.170    0.000  618.327    0.000 layer.py:76(move)
               15347818   33.680    0.000  611.032    0.000 linear.py:93(forward)
               15347818   12.474    0.000  559.933    0.000 functional.py:1737(linear)
               15347818  544.419    0.000  544.419    0.000 {built-in method torch._C._nn.linear}
                4156294   36.625    0.000  539.591    0.000 agent.py:55(modify_board)
               12793102  466.850    0.000  466.850    0.000 {built-in method cat}
                1439468   35.951    0.000  398.586    0.000 replaybuffer.py:19(stacker)
               71973400   51.782    0.000  363.633    0.000 layers.py:486(isFree)
                4156294  346.614    0.000  346.614    0.000 {built-in method torch._C._nn.one_hot}
               20943580   19.752    0.000  319.785    0.000 activation.py:713(forward)
                 719734   13.459    0.000  314.671    0.000 agent.py:105(__call__)
              205191272  279.053    0.000  311.850    0.000 layer.py:73(isFree)
               31600150  304.494    0.000  304.494    0.000 {built-in method clone}
               20943580   18.098    0.000  300.032    0.000 functional.py:1364(leaky_relu)
               20943580  278.464    0.000  278.464    0.000 {built-in method torch._C._nn.leaky_relu}
               40305104  273.470    0.000  273.470    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2159202   45.531    0.000  247.692    0.000 optimizer.py:189(zero_grad)
               40305104  244.971    0.000  244.971    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2159205  128.689    0.000  212.236    0.000 layer.py:137(NoRock_update)
                3876604  202.733    0.000  202.733    0.000 {built-in method tensor}
               71973500   20.571    0.000  199.014    0.000 {built-in method builtins.all}
              216156289   52.203    0.000  187.107    0.000 layers.py:452(<genexpr>)
                2716826   64.573    0.000  178.628    0.000 exploration.py:53(softmaxer)
               20152552  162.868    0.000  162.868    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2159202    3.194    0.000  157.102    0.000 game.py:23(board)
                 719734   85.943    0.000  145.813    0.000 collector.py:54(collect)
               20152552  143.479    0.000  143.479    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               20152552  130.982    0.000  130.982    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               20152552  130.006    0.000  130.006    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               71973500   88.001    0.000  128.928    0.000 layers.py:110(isDone)
              141067948   94.903    0.000  118.045    0.000 tensor.py:906(grad)
                1439468   44.645    0.000  113.143    0.000 random.py:315(sample)
                 465200    4.234    0.000  108.364    0.000 layers.py:496(restart)
                2159202    4.082    0.000  102.106    0.000 loss.py:527(forward)
                2159202   10.143    0.000   98.024    0.000 functional.py:2898(mse_loss)
               20152552   96.819    0.000   96.819    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               71973400   58.294    0.000   74.703    0.000 layers.py:492(check)
               35036710   74.134    0.000   74.134    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 465200    2.660    0.000   73.249    0.000 level.py:8(__init__)
                6477606   68.916    0.000   68.916    0.000 {built-in method sum}
        544093847/544093844   51.157    0.000   67.125    0.000 {built-in method builtins.len}
                 465200    4.068    0.000   60.472    0.000 levels.py:122(generate)
                2159202   58.773    0.000   58.773    0.000 {built-in method torch._C._nn.mse_loss}
                2716826   58.015    0.000   58.015    0.000 {built-in method multinomial}
                3598670    5.123    0.000   54.844    0.000 tensor.py:525(__rsub__)
               82428936   38.057    0.000   53.372    0.000 layer.py:100(add)
               11191524    7.825    0.000   52.880    0.000 flatten.py:39(forward)
                2159544   52.812    0.000   52.812    0.000 {built-in method max}
                1395600   12.859    0.000   52.327    0.000 level.py:41(notUsed)
              168790258   52.101    0.000   52.101    0.000 layer.py:116(elements)
               66608936   34.861    0.000   51.739    0.000 layer.py:96(remove)
                 719734    4.132    0.000   50.051    0.000 exploration.py:47(epsilonGreedy)
                3598670   48.858    0.000   48.858    0.000 {built-in method rsub}
               73389869   31.207    0.000   46.717    0.000 random.py:250(_randbelow_with_getrandbits)
                1439470   45.298    0.000   45.298    0.000 {built-in method nonzero}
               11191524   45.055    0.000   45.055    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               58680159   42.395    0.000   42.398    0.000 module.py:934(__getattr__)
                2159202    9.685    0.000   42.061    0.000 __init__.py:28(_make_grads)
               73465182   40.749    0.000   40.749    0.000 {built-in method torch._C._get_tracing_state}
                2159202   40.723    0.000   40.723    0.000 {built-in method gather}
                4318404    9.512    0.000   40.143    0.000 profiler.py:615(__enter__)
              426705547   38.531    0.000   38.531    0.000 layer.py:69(positions)
                3152896   37.823    0.000   37.823    0.000 {method 'long' of 'torch._C._TensorBase' objects}
                5038142   35.443    0.000   35.443    0.000 {built-in method zeros}
                2717097    3.607    0.000   34.479    0.000 functional.py:1553(softmax)
                4318404    5.846    0.000   32.761    0.000 profiler.py:607(__init__)
              111980703   22.532    0.000   32.381    0.000 enum.py:646(__hash__)
                4318404   30.631    0.000   30.631    0.000 {built-in method torch._ops.profiler._record_function_enter}
                2159202   30.551    0.000   30.551    0.000 {built-in method ones_like}
              335344540   30.469    0.000   30.469    0.000 {method 'append' of 'list' objects}
                2717097   30.451    0.000   30.451    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9457745: <test_METAk500000_0> in cluster <dcc> Done

Job <test_METAk500000_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:24:29 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 17:24:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 17:24:29 2021
Terminated at Wed Mar 24 21:20:00 2021
Results reported at Wed Mar 24 21:20:00 2021

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

    CPU time :                                   14078.75 sec.
    Max Memory :                                 5000 MB
    Average Memory :                             4306.83 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3192.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14146 sec.
    Turnaround time :                            14131 sec.

The output (if any) is above this job summary.

