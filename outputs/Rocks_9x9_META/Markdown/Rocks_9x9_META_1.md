
# Parameters

    Name :                      Rocks_9x9_META-1
    Main :                      metateleport
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
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      16254283646 function calls (16157662911 primitive calls) in 39318.63 seconds

##    Ordered by: cumulative time
   List reduced from 469 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39318.631 39318.631 {built-in method builtins.exec}
                      1    4.870    4.870 39318.631 39318.631 <string>:1(<module>)
                      1   81.739   81.739 39313.761 39313.761 main.py:14(metateleport)
                2100574 5873.916    0.003 10763.070    0.005 replaybuffer.py:27(teleporter_save_data)
                3150861   11.983    0.000 9543.644    0.003 agent.py:27(learn)
                3150861  231.636    0.000 7885.426    0.003 learner.py:42(Qlearn)
                2100574   69.789    0.000 7111.796    0.003 agent.py:51(_learn)
                1050287    5.471    0.000 6450.362    0.006 game.py:27(step)
                1050287    6.956    0.000 6200.921    0.006 layers.py:373(step)
                2100574 4438.860    0.002 5950.351    0.003 agent.py:81(interveen)
                1050287   89.123    0.000 4558.219    0.004 layers.py:18(step)
              105028700  278.669    0.000 4460.664    0.000 layer.py:74(move)
        108171579/11552543  453.659    0.000 3973.334    0.000 module.py:866(_call_impl)
              333183038 3949.257    0.000 3949.257    0.000 {built-in method clone}
                2100574 3100.183    0.001 3817.868    0.002 replaybuffer.py:23(sample_data)
                8401682   23.925    0.000 3716.779    0.000 network.py:24(forward)
                8401682  119.708    0.000 3638.718    0.000 container.py:117(forward)
                3150861   28.114    0.000 3320.143    0.001 optimizer.py:84(wrapper)
                3150861   13.416    0.000 3190.005    0.001 grad_mode.py:24(decorate_context)
              105028700  307.606    0.000 3172.839    0.000 layers.py:390(check)
                3150861   97.320    0.000 3145.842    0.001 adam.py:55(step)
                4200534  103.620    0.000 3018.557    0.001 agent.py:46(__call__)
                3150861  652.382    0.000 2942.428    0.001 _functional.py:53(adam)
                1050287   29.713    0.000 2411.641    0.002 agent.py:145(_learn)
                3150861   16.197    0.000 1985.985    0.001 tensor.py:195(backward)
                3150861   12.904    0.000 1969.311    0.001 __init__.py:68(backward)
                3150861 1886.402    0.001 1886.402    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              105028700 1565.494    0.000 1662.057    0.000 layers.py:76(check)
                1050287 1051.195    0.001 1656.224    0.002 agent.py:101(metamodify)
                1050288  117.690    0.000 1626.835    0.002 layers.py:344(update)
               16803364   37.023    0.000 1300.101    0.000 conv.py:398(forward)
               16803364   23.543    0.000 1246.302    0.000 conv.py:390(_conv_forward)
               16803364 1222.759    0.000 1222.759    0.000 {built-in method conv2d}
               23104472   47.478    0.000 1050.971    0.000 linear.py:93(forward)
              338433859  988.182    0.000  988.182    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               23104472   18.453    0.000  980.074    0.000 functional.py:1737(linear)
               23104472  956.771    0.000  956.771    0.000 {built-in method torch._C._nn.linear}
                6301108   62.538    0.000  914.197    0.000 agent.py:55(modify_board)
              105028700  157.209    0.000  874.111    0.000 layers.py:384(isFree)
                9452592  464.726    0.000  770.714    0.000 layer.py:119(update)
               18904552  722.165    0.000  722.165    0.000 {built-in method cat}
              785807844  620.609    0.000  716.902    0.000 layer.py:71(isFree)
               58816072  599.853    0.000  599.853    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               31506154   24.842    0.000  586.725    0.000 activation.py:713(forward)
                2100574   41.869    0.000  574.681    0.000 replaybuffer.py:19(stacker)
                6301108  570.487    0.000  570.487    0.000 {built-in method torch._C._nn.one_hot}
               31506154   26.269    0.000  561.883    0.000 functional.py:1364(leaky_relu)
               31506154  530.175    0.000  530.175    0.000 {built-in method torch._C._nn.leaky_relu}
               58816072  521.151    0.000  521.151    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1050287   16.802    0.000  483.043    0.000 agent.py:140(__call__)
                5443265  476.022    0.000  476.022    0.000 {built-in method tensor}
                3150861   75.710    0.000  467.235    0.000 optimizer.py:189(zero_grad)
                1262280   13.153    0.000  425.634    0.000 layers.py:394(restart)
                3150861    4.266    0.000  406.157    0.000 game.py:23(board)
             1596783718  263.462    0.000  371.649    0.000 enum.py:646(__hash__)
               29408036  337.122    0.000  337.122    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4200534  115.150    0.000  312.457    0.000 exploration.py:53(softmaxer)
                1050287  177.619    0.000  292.381    0.000 collector.py:54(collect)
               29408036  286.966    0.000  286.966    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1262280    7.316    0.000  272.103    0.000 level.py:8(__init__)
               29408036  270.011    0.000  270.011    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              105028800   28.273    0.000  269.496    0.000 {built-in method builtins.all}
               29408036  266.080    0.000  266.080    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              105028700  165.861    0.000  265.126    0.000 layers.py:216(check)
              105028700  164.887    0.000  261.988    0.000 layers.py:244(check)
              105028700  208.440    0.000  259.534    0.000 layers.py:63(check)
              105028700  159.443    0.000  258.996    0.000 layers.py:230(check)
              315166347   71.847    0.000  252.855    0.000 layers.py:350(<genexpr>)
                1262280   40.862    0.000  242.238    0.000 levels.py:95(generate)
             2467087801  215.290    0.000  215.290    0.000 layer.py:67(positions)
               29408036  210.802    0.000  210.802    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              403918347  195.212    0.000  195.212    0.000 layer.py:114(elements)
              205856336  143.628    0.000  177.325    0.000 tensor.py:906(grad)
                3362854   66.510    0.000  175.715    0.000 random.py:315(sample)
              105028800  118.113    0.000  171.827    0.000 layers.py:110(isDone)
                3150861    4.517    0.000  153.508    0.000 loss.py:527(forward)
                3150861   11.813    0.000  148.991    0.000 functional.py:2898(mse_loss)
                2524560   16.317    0.000  145.312    0.000 level.py:41(notUsed)
               11360520   16.495    0.000  136.933    0.000 layer.py:48(restart)
                9452583  132.070    0.000  132.070    0.000 {built-in method sum}
              105028700   86.811    0.000  131.513    0.000 layers.py:203(check)
        1279496949/1279496946  104.056    0.000  130.987    0.000 {built-in method builtins.len}
             1596796185  108.189    0.000  108.189    0.000 {built-in method builtins.hash}
              192645815   73.353    0.000   99.312    0.000 layer.py:98(add)
                3150861   98.359    0.000   98.359    0.000 {built-in method torch._C._nn.mse_loss}
                4200534   98.353    0.000   98.353    0.000 {built-in method multinomial}
               16803364   11.635    0.000   95.946    0.000 flatten.py:39(forward)
                5251435    7.484    0.000   95.825    0.000 tensor.py:525(__rsub__)
                5251435   86.928    0.000   86.928    0.000 {built-in method rsub}
               69425400   85.909    0.000   85.909    0.000 level.py:32(inverse)
                3151386   85.861    0.000   85.861    0.000 {built-in method max}
               16803364   84.311    0.000   84.311    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1262380   30.731    0.000   81.202    0.000 layers.py:33(reset)
               96462300   48.648    0.000   79.915    0.000 layer.py:94(remove)
              136612944   53.838    0.000   78.297    0.000 random.py:250(_randbelow_with_getrandbits)
              110272993   76.096    0.000   76.096    0.000 {built-in method torch._C._get_tracing_state}
              785807844   73.959    0.000   73.959    0.000 layer.py:175(isBlocking)
                2100576   73.401    0.000   73.401    0.000 {built-in method nonzero}
                3150861   68.649    0.000   68.649    0.000 {built-in method gather}
                3150861   12.272    0.000   67.293    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9452863: <Rocks_9x9_META_1> in cluster <dcc> Done

Job <Rocks_9x9_META_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar 23 02:18:34 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar 23 02:18:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 23 02:18:36 2021
Terminated at Tue Mar 23 13:14:05 2021
Results reported at Tue Mar 23 13:14:05 2021

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

    CPU time :                                   39291.54 sec.
    Max Memory :                                 3764 MB
    Average Memory :                             3710.46 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               4428.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39444 sec.
    Turnaround time :                            39331 sec.

The output (if any) is above this job summary.

