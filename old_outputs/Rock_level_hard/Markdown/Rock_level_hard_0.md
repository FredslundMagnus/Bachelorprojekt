
# Parameters

    Name :                      Rock_level_hard-0
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
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      38516723235 function calls (38384565964 primitive calls) in 39314.53 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39314.526 39314.526 {built-in method builtins.exec}
                      1    0.909    0.909 39314.526 39314.526 <string>:1(<module>)
                      1   95.065   95.065 39313.617 39313.617 main.py:13(teleport)
                2359957    8.254    0.000 15770.628    0.007 game.py:27(step)
                2359957   10.521    0.000 15278.859    0.006 layers.py:373(step)
                2359957  180.672    0.000 10424.285    0.004 layers.py:18(step)
              235995700  478.908    0.000 10223.145    0.000 layer.py:74(move)
                4719914   16.566    0.000 9793.653    0.002 agent.py:26(learn)
                4719914  261.985    0.000 8246.270    0.002 learner.py:42(Qlearn)
              235995700  707.442    0.000 7888.958    0.000 layers.py:390(check)
                2359957   74.971    0.000 5852.931    0.002 agent.py:50(_learn)
                2359957 3310.503    0.001 5597.653    0.002 replaybuffer.py:27(teleporter_save_data)
                2359958  234.201    0.000 4829.565    0.002 layers.py:344(update)
              235995700 3960.463    0.000 4560.862    0.000 layers.py:76(check)
        148675848/16519588  530.519    0.000 4367.278    0.000 module.py:866(_call_impl)
               11799674   31.924    0.000 4057.320    0.000 network.py:24(forward)
               11799674  129.930    0.000 3958.420    0.000 container.py:117(forward)
                2359957   65.397    0.000 3915.322    0.002 agent.py:101(_learn)
                2359957 2280.793    0.001 3621.701    0.002 agent.py:77(interveen)
                4719914   36.581    0.000 3212.944    0.001 optimizer.py:84(wrapper)
                4719914   17.946    0.000 3050.037    0.001 grad_mode.py:24(decorate_context)
                4719914  116.528    0.000 2992.779    0.001 adam.py:55(step)
                4719914  626.379    0.000 2731.633    0.001 _functional.py:53(adam)
                4719803   99.523    0.000 2710.842    0.001 agent.py:45(__call__)
                4719914   16.896    0.000 2107.405    0.000 tensor.py:195(backward)
                4719914   16.912    0.000 2089.925    0.000 __init__.py:68(backward)
                4719914 1989.461    0.000 1989.461    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7143181   62.985    0.000 1965.822    0.000 layers.py:394(restart)
               21239622 1304.080    0.000 1942.798    0.000 layer.py:119(update)
              236925548 1876.179    0.000 1876.179    0.000 {built-in method clone}
              235995700  371.682    0.000 1634.335    0.000 layers.py:384(isFree)
                2359957  822.927    0.000 1545.381    0.001 replaybuffer.py:23(sample_data)
               23599348   49.213    0.000 1485.822    0.000 conv.py:398(forward)
                2359957  880.378    0.000 1436.936    0.001 agent.py:59(modify)
               23599348   27.373    0.000 1415.816    0.000 conv.py:390(_conv_forward)
               23599348 1388.443    0.000 1388.443    0.000 {built-in method conv2d}
             1818303899 1030.299    0.000 1262.653    0.000 layer.py:71(isFree)
                7143181   27.929    0.000 1245.199    0.000 level.py:8(__init__)
                7143181  175.945    0.000 1116.095    0.000 levels.py:95(generate)
               30679108   58.632    0.000 1102.208    0.000 linear.py:93(forward)
               30679108   23.171    0.000 1017.162    0.000 functional.py:1737(linear)
               30679108  988.132    0.000  988.132    0.000 {built-in method torch._C._nn.linear}
             3999703099  662.390    0.000  960.454    0.000 enum.py:646(__hash__)
                2359957   29.195    0.000  842.505    0.000 agent.py:96(__call__)
                7079760   38.160    0.000  837.316    0.000 agent.py:54(modify_board)
                9765216  704.892    0.000  704.892    0.000 {built-in method tensor}
               21239502  695.651    0.000  695.651    0.000 {built-in method cat}
               64288629   89.962    0.000  638.345    0.000 layer.py:48(restart)
              235995700  376.239    0.000  612.846    0.000 layers.py:216(check)
               14286362   80.966    0.000  611.687    0.000 level.py:41(notUsed)
              235995700  361.553    0.000  598.281    0.000 layers.py:230(check)
              235995700  369.807    0.000  596.541    0.000 layers.py:244(check)
              235995800   65.938    0.000  596.153    0.000 {built-in method builtins.all}
                4719914    4.599    0.000  586.696    0.000 game.py:23(board)
               42478782   30.242    0.000  584.558    0.000 activation.py:713(forward)
                2359957   39.246    0.000  567.571    0.000 replaybuffer.py:19(stacker)
              731108414  169.475    0.000  557.077    0.000 layers.py:350(<genexpr>)
                7079760  555.242    0.000  555.242    0.000 {built-in method torch._C._nn.one_hot}
               42478782   31.639    0.000  554.317    0.000 functional.py:1364(leaky_relu)
               84958452  523.754    0.000  523.754    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42478782  516.414    0.000  516.414    0.000 {built-in method torch._C._nn.leaky_relu}
             5488838171  499.363    0.000  499.363    0.000 layer.py:67(positions)
                4719914   85.784    0.000  479.329    0.000 optimizer.py:189(zero_grad)
               84958452  472.990    0.000  472.990    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              235995700  295.672    0.000  454.489    0.000 layers.py:63(check)
              955779349  334.813    0.000  450.045    0.000 layer.py:98(add)
              244005308  449.628    0.000  449.628    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1949087779  428.866    0.000  428.866    0.000 layer.py:114(elements)
              441808823  195.472    0.000  404.938    0.000 layer.py:94(remove)
                9503138  132.908    0.000  370.791    0.000 random.py:315(sample)
              235995800  239.199    0.000  364.781    0.000 layers.py:110(isDone)
                7143281  172.152    0.000  346.494    0.000 layers.py:33(reset)
              357159050  323.835    0.000  323.835    0.000 level.py:32(inverse)
                2359957  187.975    0.000  319.038    0.000 collector.py:54(collect)
               42479226  316.387    0.000  316.387    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              235995700  191.437    0.000  298.393    0.000 layers.py:203(check)
             3999720418  298.066    0.000  298.066    0.000 {built-in method builtins.hash}
               42479226  273.101    0.000  273.101    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4719803  101.968    0.000  273.085    0.000 exploration.py:53(softmaxer)
               42479226  255.696    0.000  255.696    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               42479226  253.037    0.000  253.037    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              297354636  182.636    0.000  227.374    0.000 tensor.py:906(grad)
              235995700   89.582    0.000  209.114    0.000 layers.py:99(<listcomp>)
        2459530691/2459530689  160.244    0.000  190.780    0.000 {built-in method builtins.len}
             2920548881  190.012    0.000  190.012    0.000 {method 'append' of 'list' objects}
               42479226  186.120    0.000  186.120    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              332351442  126.511    0.000  183.065    0.000 random.py:250(_randbelow_with_getrandbits)
                4719914    5.764    0.000  182.996    0.000 loss.py:527(forward)
             1818303899  177.969    0.000  177.969    0.000 layer.py:175(isBlocking)
                4719914   16.437    0.000  177.232    0.000 functional.py:2898(mse_loss)
              441808823  175.845    0.000  175.845    0.000 {method 'remove' of 'list' objects}
               14286362   11.455    0.000  158.487    0.000 level.py:38(elementsIn)
               14159742  137.553    0.000  137.553    0.000 {built-in method sum}
                4719914  108.929    0.000  108.929    0.000 {built-in method torch._C._nn.mse_loss}
               23599348   15.148    0.000  101.945    0.000 flatten.py:39(forward)
                4720620  100.489    0.000  100.489    0.000 {built-in method max}
                7079871    9.085    0.000   94.786    0.000 tensor.py:525(__rsub__)
               14286362   46.390    0.000   90.071    0.000 level.py:39(<listcomp>)
               23599348   86.798    0.000   86.798    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4719803   85.903    0.000   85.903    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9444621: <Rock_level_hard_0> in cluster <dcc> Done

Job <Rock_level_hard_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:57 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 02:08:58 2021
Terminated at Sun Mar 21 13:04:24 2021
Results reported at Sun Mar 21 13:04:24 2021

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

    CPU time :                                   39210.57 sec.
    Max Memory :                                 5646 MB
    Average Memory :                             4168.02 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2546.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39355 sec.
    Turnaround time :                            39327 sec.

The output (if any) is above this job summary.

