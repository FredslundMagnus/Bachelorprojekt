
# Parameters

    Name :                      Rock_level_hard_resethigh-0
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
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      39995557217 function calls (39858069934 primitive calls) in 39309.73 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39309.732 39309.732 {built-in method builtins.exec}
                      1    0.944    0.944 39309.732 39309.732 <string>:1(<module>)
                      1   98.656   98.656 39308.788 39308.788 main.py:13(teleport)
                2455133    8.285    0.000 16398.208    0.007 game.py:27(step)
                2455133   11.685    0.000 15884.883    0.006 layers.py:373(step)
                2455133  189.871    0.000 10740.990    0.004 layers.py:18(step)
              245513300  494.873    0.000 10530.661    0.000 layer.py:74(move)
                4910266   16.086    0.000 10300.352    0.002 agent.py:26(learn)
                4910266  279.206    0.000 8668.864    0.002 learner.py:42(Qlearn)
              245513300  742.814    0.000 8154.277    0.000 layers.py:390(check)
                2455133   78.303    0.000 6157.827    0.003 agent.py:50(_learn)
                2455134  249.600    0.000 5117.584    0.002 layers.py:344(update)
              245513300 4154.186    0.000 4736.805    0.000 layers.py:76(check)
        154672105/17185833  570.814    0.000 4631.939    0.000 module.py:866(_call_impl)
                2455133 2679.452    0.001 4571.567    0.002 replaybuffer.py:27(teleporter_save_data)
               12275567   33.041    0.000 4299.795    0.000 network.py:24(forward)
               12275567  137.985    0.000 4194.738    0.000 container.py:117(forward)
                2455133   68.474    0.000 4117.506    0.002 agent.py:101(_learn)
                4910266   38.667    0.000 3347.605    0.001 optimizer.py:84(wrapper)
                2455133 1878.564    0.001 3296.457    0.001 agent.py:77(interveen)
                4910266   18.726    0.000 3176.194    0.001 grad_mode.py:24(decorate_context)
                4910266  128.412    0.000 3113.546    0.001 adam.py:55(step)
                4910168  103.788    0.000 2864.953    0.001 agent.py:45(__call__)
                4910266  647.732    0.000 2829.856    0.001 _functional.py:53(adam)
                4910266   18.526    0.000 2213.387    0.000 tensor.py:195(backward)
                4910266   18.198    0.000 2194.232    0.000 __init__.py:68(backward)
                7752482   64.862    0.000 2138.392    0.000 layers.py:394(restart)
                4910266 2087.742    0.000 2087.742    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               22096206 1361.331    0.000 2021.306    0.000 layer.py:119(update)
              245513300  366.468    0.000 1666.560    0.000 layers.py:384(isFree)
                2455133  852.633    0.000 1613.074    0.001 replaybuffer.py:23(sample_data)
               24551134   54.029    0.000 1576.891    0.000 conv.py:398(forward)
              190199530 1556.489    0.000 1556.489    0.000 {built-in method clone}
                2455133  924.802    0.000 1504.999    0.001 agent.py:59(modify)
               24551134   29.905    0.000 1500.736    0.000 conv.py:390(_conv_forward)
               24551134 1470.831    0.000 1470.831    0.000 {built-in method conv2d}
                7752482   30.176    0.000 1359.316    0.000 level.py:8(__init__)
             1894791041 1076.058    0.000 1300.092    0.000 layer.py:71(isFree)
                7752482  187.573    0.000 1218.065    0.000 levels.py:95(generate)
               31916435   63.339    0.000 1159.057    0.000 linear.py:93(forward)
               31916435   25.366    0.000 1067.644    0.000 functional.py:1737(linear)
               31916435 1036.229    0.000 1036.229    0.000 {built-in method torch._C._nn.linear}
             4194334538  693.718    0.000  996.607    0.000 enum.py:646(__hash__)
                2455133   30.258    0.000  891.335    0.000 agent.py:96(__call__)
                7365301   40.559    0.000  876.176    0.000 agent.py:54(modify_board)
               10155771  737.151    0.000  737.151    0.000 {built-in method tensor}
               22096099  731.630    0.000  731.630    0.000 {built-in method cat}
               69772338  100.856    0.000  693.233    0.000 layer.py:48(restart)
               15504964   89.295    0.000  670.457    0.000 level.py:41(notUsed)
              245513300  388.118    0.000  629.560    0.000 layers.py:216(check)
               44192002   32.223    0.000  625.081    0.000 activation.py:713(forward)
                4910266    5.254    0.000  613.738    0.000 game.py:23(board)
              245513400   67.000    0.000  613.326    0.000 {built-in method builtins.all}
              245513300  371.640    0.000  611.304    0.000 layers.py:230(check)
                2455133   40.566    0.000  597.896    0.000 replaybuffer.py:19(stacker)
              245513300  364.812    0.000  594.379    0.000 layers.py:244(check)
               44192002   35.020    0.000  592.859    0.000 functional.py:1364(leaky_relu)
                7365301  581.062    0.000  581.062    0.000 {built-in method torch._C._nn.one_hot}
              752818889  170.642    0.000  573.924    0.000 layers.py:350(<genexpr>)
               44192002  550.960    0.000  550.960    0.000 {built-in method torch._C._nn.leaky_relu}
               88384788  539.419    0.000  539.419    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4910266   94.638    0.000  509.303    0.000 optimizer.py:189(zero_grad)
             5711028515  501.408    0.000  501.408    0.000 layer.py:67(positions)
               88384788  490.997    0.000  490.997    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              245513300  315.207    0.000  474.153    0.000 layers.py:63(check)
              987064826  338.636    0.000  458.885    0.000 layer.py:98(add)
             2013537316  440.597    0.000  440.597    0.000 layer.py:114(elements)
               10207615  143.796    0.000  401.262    0.000 random.py:315(sample)
              197564831  384.054    0.000  384.054    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              423008718  180.029    0.000  382.004    0.000 layer.py:94(remove)
              245513400  250.756    0.000  379.899    0.000 layers.py:110(isDone)
                7752582  188.244    0.000  376.216    0.000 layers.py:33(reset)
              387624100  352.475    0.000  352.475    0.000 level.py:32(inverse)
                2455133  195.515    0.000  333.672    0.000 collector.py:54(collect)
               44192394  332.336    0.000  332.336    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              245513300  197.143    0.000  305.009    0.000 layers.py:203(check)
             4194352577  302.893    0.000  302.893    0.000 {built-in method builtins.hash}
                4910168  107.644    0.000  286.388    0.000 exploration.py:53(softmaxer)
               44192394  282.153    0.000  282.153    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               44192394  265.429    0.000  265.429    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               44192394  261.523    0.000  261.523    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              309346812  195.978    0.000  242.429    0.000 tensor.py:906(grad)
              245513300   95.719    0.000  206.296    0.000 layers.py:99(<listcomp>)
        2574702888/2574702886  172.691    0.000  205.235    0.000 {built-in method builtins.len}
              355392301  138.829    0.000  199.845    0.000 random.py:250(_randbelow_with_getrandbits)
             3002933747  199.135    0.000  199.135    0.000 {method 'append' of 'list' objects}
               44192394  194.140    0.000  194.140    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4910266    7.188    0.000  192.140    0.000 loss.py:527(forward)
                4910266   17.077    0.000  184.951    0.000 functional.py:2898(mse_loss)
               15504964   13.047    0.000  174.984    0.000 level.py:38(elementsIn)
             1894791041  169.066    0.000  169.066    0.000 layer.py:175(isBlocking)
              423008718  168.661    0.000  168.661    0.000 {method 'remove' of 'list' objects}
               14730798  144.443    0.000  144.443    0.000 {built-in method sum}
                4910266  113.802    0.000  113.802    0.000 {built-in method torch._C._nn.mse_loss}
               24551134   17.092    0.000  108.786    0.000 flatten.py:39(forward)
                4911002  106.337    0.000  106.337    0.000 {built-in method max}
                7365399    9.479    0.000   99.881    0.000 tensor.py:525(__rsub__)
               15504964   50.425    0.000   98.958    0.000 level.py:39(<listcomp>)
               24551134   91.695    0.000   91.695    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7752482   42.035    0.000   90.036    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9444629: <Rock_level_hard_resethigh_0> in cluster <dcc> Done

Job <Rock_level_hard_resethigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:27 2021
Terminated at Mon Mar 22 00:00:36 2021
Results reported at Mon Mar 22 00:00:36 2021

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

    CPU time :                                   39211.00 sec.
    Max Memory :                                 5765 MB
    Average Memory :                             4205.24 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2427.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39319 sec.
    Turnaround time :                            78698 sec.

The output (if any) is above this job summary.

