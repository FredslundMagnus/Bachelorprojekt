
# Parameters

    Name :                      causal2_9x9-1
    Main :                      teleport
    Level :                     Levels.Causal2
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
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      27957558664 function calls (27862108985 primitive calls) in 35710.73 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.730 35710.730 {built-in method builtins.exec}
                      1    0.982    0.982 35710.730 35710.730 <string>:1(<module>)
                      1   90.985   90.985 35709.748 35709.748 main.py:13(teleport)
                3408944   13.846    0.000 9438.868    0.003 agent.py:26(learn)
                1704472    8.104    0.000 8792.793    0.005 game.py:27(step)
                1704472    9.924    0.000 8387.629    0.005 layers.py:373(step)
                3408944  227.048    0.000 8053.202    0.002 learner.py:42(Qlearn)
                1704472 4663.493    0.003 8030.092    0.005 replaybuffer.py:27(teleporter_save_data)
                1704472   55.265    0.000 5638.624    0.003 agent.py:50(_learn)
                1704472  140.986    0.000 4950.107    0.003 layers.py:18(step)
              170447200  413.181    0.000 4794.746    0.000 layer.py:74(move)
                1704472 3477.919    0.002 4703.541    0.003 agent.py:77(interveen)
        107379825/11931157  420.226    0.000 4003.400    0.000 module.py:715(_call_impl)
                1704472   48.828    0.000 3779.222    0.002 agent.py:101(_learn)
                8522213   20.983    0.000 3733.200    0.000 network.py:24(forward)
                8522213  101.881    0.000 3657.929    0.000 container.py:115(forward)
                1704473  186.870    0.000 3412.090    0.002 layers.py:344(update)
                3408944   21.002    0.000 3210.030    0.001 grad_mode.py:23(decorate_context)
                3408944  110.691    0.000 3149.033    0.001 adam.py:55(step)
              170447200  462.575    0.000 2768.329    0.000 layers.py:390(check)
              267534206 2648.150    0.000 2648.150    0.000 {built-in method clone}
                3408944  575.974    0.000 2576.577    0.001 functional.py:53(adam)
                3408797   81.686    0.000 2467.425    0.001 agent.py:45(__call__)
                1704472 1066.660    0.001 1919.797    0.001 replaybuffer.py:23(sample_data)
                3408944   20.144    0.000 1886.573    0.001 tensor.py:181(backward)
                3408944   12.183    0.000 1866.430    0.001 __init__.py:68(backward)
                3408944 1775.765    0.001 1775.765    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1704472  725.317    0.000 1432.876    0.001 agent.py:59(modify)
                4374693   44.411    0.000 1366.972    0.000 layers.py:394(restart)
               17044426   30.954    0.000 1353.512    0.000 conv.py:422(forward)
              170447200  301.336    0.000 1330.473    0.000 layers.py:384(isFree)
               15340257  806.663    0.000 1313.809    0.000 layer.py:119(update)
               17044426   34.829    0.000 1308.992    0.000 conv.py:414(_conv_forward)
               17044426 1267.910    0.000 1267.910    0.000 {built-in method conv2d}
               22157695   49.121    0.000 1160.141    0.000 linear.py:92(forward)
               22157695   81.913    0.000 1086.794    0.000 functional.py:1669(linear)
             1499144368  845.660    0.000 1029.137    0.000 layer.py:71(isFree)
                4374693   20.359    0.000  996.715    0.000 level.py:8(__init__)
                4374693   54.132    0.000  906.106    0.000 levels.py:151(generate)
               15340101  847.706    0.000  847.706    0.000 {built-in method cat}
              214763526  495.995    0.000  825.394    0.000 tensor.py:933(grad)
               24497383  179.903    0.000  795.319    0.000 level.py:41(notUsed)
                1704472   23.537    0.000  766.306    0.000 agent.py:96(__call__)
               22157695  765.449    0.000  765.449    0.000 {built-in method addmm}
                5113269   33.955    0.000  746.327    0.000 agent.py:54(modify_board)
             2895809673  508.543    0.000  733.631    0.000 enum.py:646(__hash__)
              272647475  725.656    0.000  725.656    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1704472   33.374    0.000  724.376    0.000 replaybuffer.py:19(stacker)
                3408944   70.921    0.000  719.595    0.000 optimizer.py:167(zero_grad)
                7075422  568.965    0.000  568.965    0.000 {built-in method tensor}
               61360992  520.750    0.000  520.750    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               30679908   27.131    0.000  513.301    0.000 activation.py:713(forward)
               30679908   40.747    0.000  486.170    0.000 functional.py:1292(leaky_relu)
              177265988   56.797    0.000  483.677    0.000 {built-in method builtins.all}
                5113269  481.649    0.000  481.649    0.000 {built-in method torch._C._nn.one_hot}
              170447200  297.050    0.000  473.142    0.000 layers.py:216(check)
              170447200  295.047    0.000  472.735    0.000 layers.py:230(check)
              170447200  296.663    0.000  469.235    0.000 layers.py:244(check)
                3408944    4.404    0.000  462.055    0.000 game.py:23(board)
              546139706  133.934    0.000  442.183    0.000 layers.py:350(<genexpr>)
               30679908  441.266    0.000  441.266    0.000 {built-in method torch._C._nn.leaky_relu}
              274420155  147.581    0.000  437.219    0.000 overrides.py:1070(has_torch_function)
               61360992  428.511    0.000  428.511    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              170447200  281.306    0.000  389.715    0.000 layers.py:76(check)
             4057862577  357.792    0.000  357.792    0.000 layer.py:67(positions)
              687492500  343.989    0.000  343.989    0.000 layer.py:114(elements)
               39372237   30.787    0.000  312.833    0.000 layer.py:48(restart)
               30680496  304.216    0.000  304.216    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1704472  177.324    0.000  303.423    0.000 collector.py:54(collect)
              170447300  196.890    0.000  289.263    0.000 layers.py:110(isDone)
               30680496  277.723    0.000  277.723    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              303395739  111.608    0.000  276.455    0.000 {built-in method builtins.any}
               24497383   17.253    0.000  265.970    0.000 level.py:38(elementsIn)
             1167740231  264.558    0.000  264.558    0.000 level.py:32(inverse)
                3408797   94.076    0.000  256.584    0.000 exploration.py:53(softmaxer)
               30680496  246.893    0.000  246.893    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              170447200  157.712    0.000  239.165    0.000 layers.py:203(check)
             2895822312  225.091    0.000  225.091    0.000 {built-in method builtins.hash}
                4374793  111.852    0.000  225.075    0.000 layers.py:33(reset)
              170447200  145.092    0.000  218.414    0.000 layers.py:63(check)
               30680496  214.214    0.000  214.214    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6818688   31.809    0.000  192.564    0.000 tensor.py:21(wrapped)
              330577905  136.896    0.000  184.344    0.000 layer.py:98(add)
                3408944    5.458    0.000  174.574    0.000 loss.py:445(forward)
                3408944   19.578    0.000  169.116    0.000 functional.py:2637(mse_loss)
               30680496  166.361    0.000  166.361    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              577816353  130.977    0.000  162.463    0.000 overrides.py:1083(<genexpr>)
               24497383   81.178    0.000  162.236    0.000 level.py:39(<listcomp>)
        1472006832/1472006830  103.136    0.000  149.605    0.000 {built-in method builtins.len}
             1499144368  141.655    0.000  141.655    0.000 layer.py:175(isBlocking)
              180913199   96.325    0.000  139.908    0.000 layer.py:94(remove)
               22157695  139.437    0.000  139.437    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1704472   47.928    0.000  125.681    0.000 random.py:315(sample)
               10226832  122.472    0.000  122.472    0.000 {built-in method sum}
                5113416   23.178    0.000  104.878    0.000 tensor.py:506(__rsub__)
                3408944   97.332    0.000   97.332    0.000 {built-in method torch._C._nn.mse_loss}
                5113416   92.825    0.000   92.825    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               17044426   12.381    0.000   92.257    0.000 flatten.py:39(forward)
                3409454   87.465    0.000   87.465    0.000 {built-in method max}
               24497383   54.051    0.000   86.482    0.000 {built-in method _functools.reduce}


Traceback (most recent call last):
  File "main.py", line 111, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9447207: <causal2_9x9_1> in cluster <dcc> Exited

Job <causal2_9x9_1> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 21 22:24:33 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 21 22:24:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 22:24:35 2021
Terminated at Mon Mar 22 08:20:00 2021
Results reported at Mon Mar 22 08:20:00 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35620.97 sec.
    Max Memory :                                 2448 MB
    Average Memory :                             2420.96 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5744.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35766 sec.
    Turnaround time :                            35727 sec.

The output (if any) is above this job summary.

