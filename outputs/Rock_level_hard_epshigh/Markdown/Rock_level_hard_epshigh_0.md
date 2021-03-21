
# Parameters

    Name :                      Rock_level_hard_epshigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      32947876909 function calls (32831162442 primitive calls) in 39315.18 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.184 39315.184 {built-in method builtins.exec}
                      1    0.958    0.958 39315.184 39315.184 <string>:1(<module>)
                      1   89.345   89.345 39314.226 39314.226 main.py:13(teleport)
                2084198    8.006    0.000 13481.151    0.006 game.py:27(step)
                2084198   10.398    0.000 12996.763    0.006 layers.py:373(step)
                4168396   14.005    0.000 11519.595    0.003 agent.py:26(learn)
                4168396  303.465    0.000 9885.269    0.002 learner.py:42(Qlearn)
                2084198  164.569    0.000 9058.116    0.004 layers.py:18(step)
              208419800  425.348    0.000 8876.456    0.000 layer.py:74(move)
                2084198   68.457    0.000 6862.006    0.003 agent.py:50(_learn)
              208419800  623.446    0.000 6839.526    0.000 layers.py:390(check)
                2084198 3150.796    0.002 5731.864    0.003 replaybuffer.py:27(teleporter_save_data)
        131302706/14589250  526.624    0.000 4738.919    0.000 module.py:866(_call_impl)
                2084198   60.526    0.000 4635.631    0.002 agent.py:101(_learn)
               10420854   28.949    0.000 4417.285    0.000 network.py:24(forward)
               10420854  139.949    0.000 4324.824    0.000 container.py:117(forward)
                4168396   35.247    0.000 4163.658    0.001 optimizer.py:84(wrapper)
              208419800 3517.127    0.000 4005.956    0.000 layers.py:76(check)
                4168396   17.199    0.000 3996.173    0.001 grad_mode.py:24(decorate_context)
                4168396  111.782    0.000 3940.505    0.001 adam.py:55(step)
                2084199  206.753    0.000 3915.853    0.002 layers.py:344(update)
                2084198 2377.608    0.001 3821.666    0.002 agent.py:77(interveen)
                4168396  814.178    0.000 3698.226    0.001 _functional.py:53(adam)
                4168260   95.305    0.000 2915.652    0.001 agent.py:45(__call__)
                4168396   16.202    0.000 2427.377    0.001 tensor.py:195(backward)
                4168396   15.604    0.000 2410.555    0.001 __init__.py:68(backward)
                4168396 2302.764    0.001 2302.764    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              177195742 2077.174    0.000 2077.174    0.000 {built-in method clone}
                2084198  999.830    0.000 1617.938    0.001 agent.py:59(modify)
               18757791 1066.331    0.000 1613.902    0.000 layer.py:119(update)
               20841708   45.704    0.000 1583.339    0.000 conv.py:398(forward)
               20841708   27.416    0.000 1517.562    0.000 conv.py:390(_conv_forward)
                5536803   46.742    0.000 1512.305    0.000 layers.py:394(restart)
               20841708 1490.146    0.000 1490.146    0.000 {built-in method conv2d}
                2084198  723.854    0.000 1444.402    0.001 replaybuffer.py:23(sample_data)
              208419800  316.314    0.000 1429.228    0.000 layers.py:384(isFree)
               27094166   56.739    0.000 1223.392    0.000 linear.py:93(forward)
               27094166   22.321    0.000 1141.569    0.000 functional.py:1737(linear)
               27094166 1113.897    0.000 1113.897    0.000 {built-in method torch._C._nn.linear}
             1615482218  918.822    0.000 1112.914    0.000 layer.py:71(isFree)
                5536803   22.148    0.000  961.450    0.000 level.py:8(__init__)
                2084198   28.159    0.000  922.316    0.000 agent.py:96(__call__)
                6252458   40.770    0.000  887.170    0.000 agent.py:54(modify_board)
                5536803  133.020    0.000  860.703    0.000 levels.py:95(generate)
             3449661972  558.589    0.000  796.951    0.000 enum.py:646(__hash__)
               75031128  746.527    0.000  746.527    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18757646  732.853    0.000  732.853    0.000 {built-in method cat}
               37515020   29.365    0.000  694.275    0.000 activation.py:713(forward)
                8825868  687.536    0.000  687.536    0.000 {built-in method tensor}
               75031128  668.279    0.000  668.279    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               37515020   30.459    0.000  664.910    0.000 functional.py:1364(leaky_relu)
               37515020  627.793    0.000  627.793    0.000 {built-in method torch._C._nn.leaky_relu}
                4168396   95.019    0.000  594.442    0.000 optimizer.py:189(zero_grad)
                2084198   37.350    0.000  582.795    0.000 replaybuffer.py:19(stacker)
                6252458  567.103    0.000  567.103    0.000 {built-in method torch._C._nn.one_hot}
              183448200  565.722    0.000  565.722    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4168396    4.730    0.000  546.456    0.000 game.py:23(board)
              208419800  325.256    0.000  519.382    0.000 layers.py:216(check)
              208419800  309.018    0.000  503.790    0.000 layers.py:244(check)
              208419900   57.584    0.000  503.610    0.000 {built-in method builtins.all}
              208419800  305.266    0.000  497.504    0.000 layers.py:230(check)
               49831227   69.925    0.000  489.778    0.000 layer.py:48(restart)
               11073606   62.899    0.000  471.708    0.000 level.py:41(notUsed)
              639276241  140.936    0.000  469.485    0.000 layers.py:350(<genexpr>)
                2084198  248.956    0.000  413.508    0.000 collector.py:54(collect)
               37515564  408.862    0.000  408.862    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4857144798  404.468    0.000  404.468    0.000 layer.py:67(positions)
              208419800  259.823    0.000  389.292    0.000 layers.py:63(check)
             1545267551  361.756    0.000  361.756    0.000 layer.py:114(elements)
               37515564  359.674    0.000  359.674    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              755463891  258.830    0.000  350.264    0.000 layer.py:98(add)
               37515564  346.181    0.000  346.181    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37515564  343.440    0.000  343.440    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              357808280  152.410    0.000  324.281    0.000 layer.py:94(remove)
              208419900  207.277    0.000  311.287    0.000 layers.py:110(isDone)
                7621001  109.369    0.000  307.107    0.000 random.py:315(sample)
                4168260  110.308    0.000  304.429    0.000 exploration.py:53(softmaxer)
               37515564  267.872    0.000  267.872    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5536903  133.968    0.000  267.189    0.000 layers.py:33(reset)
              276840150  251.518    0.000  251.518    0.000 level.py:32(inverse)
              208419800  163.013    0.000  251.105    0.000 layers.py:203(check)
             3449677347  238.364    0.000  238.364    0.000 {built-in method builtins.hash}
              262609002  177.799    0.000  219.721    0.000 tensor.py:906(grad)
                4168396    5.573    0.000  198.648    0.000 loss.py:527(forward)
                4168396   15.341    0.000  193.075    0.000 functional.py:2898(mse_loss)
        2187717737/2187717735  153.407    0.000  184.124    0.000 {built-in method builtins.len}
               12505188  174.780    0.000  174.780    0.000 {built-in method sum}
              208419800   75.419    0.000  169.434    0.000 layers.py:99(<listcomp>)
             2331829369  153.704    0.000  153.704    0.000 {method 'append' of 'list' objects}
              270365461  103.158    0.000  149.036    0.000 random.py:250(_randbelow_with_getrandbits)
             1615482218  148.432    0.000  148.432    0.000 layer.py:175(isBlocking)
              357808280  143.970    0.000  143.970    0.000 {method 'remove' of 'list' objects}
                4168396  127.213    0.000  127.213    0.000 {built-in method torch._C._nn.mse_loss}
               20841708   16.222    0.000  122.870    0.000 flatten.py:39(forward)
               11073606    9.002    0.000  120.419    0.000 level.py:38(elementsIn)
                6252594    9.189    0.000  112.695    0.000 tensor.py:525(__rsub__)
                4169020  111.188    0.000  111.188    0.000 {built-in method max}
               20841708  106.648    0.000  106.648    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6252594  101.910    0.000  101.910    0.000 {built-in method rsub}
                4168260   97.892    0.000   97.892    0.000 {built-in method multinomial}


Traceback (most recent call last):
  File "main.py", line 111, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9444624: <Rock_level_hard_epshigh_0> in cluster <dcc> Exited

Job <Rock_level_hard_epshigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:57 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 02:08:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 02:08:59 2021
Terminated at Sun Mar 21 13:04:26 2021
Results reported at Sun Mar 21 13:04:26 2021

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

    CPU time :                                   39208.39 sec.
    Max Memory :                                 5301 MB
    Average Memory :                             3957.14 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2891.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39356 sec.
    Turnaround time :                            39329 sec.

The output (if any) is above this job summary.

