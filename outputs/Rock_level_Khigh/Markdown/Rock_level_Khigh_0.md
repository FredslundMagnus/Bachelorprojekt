
# Parameters

    Name :                      Rock_level_Khigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
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
    K :                         1000000.0
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
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      34756931654 function calls (34633655327 primitive calls) in 42916.45 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42916.452 42916.452 {built-in method builtins.exec}
                      1    0.972    0.972 42916.452 42916.452 <string>:1(<module>)
                      1  158.158  158.158 42915.480 42915.480 main.py:13(teleport)
                2201469   13.157    0.000 16912.955    0.008 game.py:27(step)
                2201469   15.804    0.000 16325.867    0.007 layers.py:373(step)
                2201469  221.254    0.000 11152.739    0.005 layers.py:18(step)
                4402938   25.707    0.000 11123.048    0.003 agent.py:26(learn)
              220146900  561.741    0.000 10911.117    0.000 layer.py:74(move)
                4402938  311.145    0.000 9276.174    0.002 learner.py:42(Qlearn)
              220146900  713.272    0.000 7809.370    0.000 layers.py:390(check)
                2201469   91.232    0.000 6545.731    0.003 agent.py:50(_learn)
                2201469 3134.967    0.001 5206.667    0.002 replaybuffer.py:27(teleporter_save_data)
                2201470  271.000    0.000 5131.109    0.002 layers.py:344(update)
        138685020/15409704  631.196    0.000 4936.559    0.000 module.py:866(_call_impl)
               11006766   36.949    0.000 4546.515    0.000 network.py:24(forward)
                2201469   78.754    0.000 4538.788    0.002 agent.py:101(_learn)
               11006766  152.487    0.000 4426.778    0.000 container.py:117(forward)
              220146900 3771.164    0.000 4281.727    0.000 layers.py:76(check)
                2201469 2199.577    0.001 3674.734    0.002 agent.py:77(interveen)
                4402938   51.859    0.000 3435.140    0.001 optimizer.py:84(wrapper)
                4402938   26.021    0.000 3229.535    0.001 grad_mode.py:24(decorate_context)
                4402938  149.045    0.000 3143.337    0.001 adam.py:55(step)
                4402359  139.151    0.000 3100.146    0.001 agent.py:45(__call__)
                4402938  658.117    0.000 2834.454    0.001 _functional.py:53(adam)
                2201469 1707.169    0.001 2500.676    0.001 replaybuffer.py:23(sample_data)
                4402938   21.646    0.000 2486.877    0.001 tensor.py:195(backward)
                4402938   24.832    0.000 2464.588    0.001 __init__.py:68(backward)
               19813230 1534.896    0.000 2342.219    0.000 layer.py:119(update)
                4402938 2336.596    0.001 2336.596    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              220146900  410.397    0.000 2246.927    0.000 layers.py:384(isFree)
             1808695777 1597.968    0.000 1836.530    0.000 layer.py:71(isFree)
                5677487   62.223    0.000 1771.625    0.000 layers.py:394(restart)
              191380386 1709.533    0.000 1709.533    0.000 {built-in method clone}
                2201469 1010.235    0.000 1693.118    0.001 agent.py:59(modify)
               22013532   55.943    0.000 1683.410    0.000 conv.py:398(forward)
               22013532   40.726    0.000 1600.384    0.000 conv.py:390(_conv_forward)
               22013532 1559.659    0.000 1559.659    0.000 {built-in method conv2d}
               28617360   66.083    0.000 1224.358    0.000 linear.py:93(forward)
               28617360   25.928    0.000 1124.533    0.000 functional.py:1737(linear)
                5677487   29.247    0.000 1100.250    0.000 level.py:8(__init__)
               28617360 1092.686    0.000 1092.686    0.000 {built-in method torch._C._nn.linear}
                2201469   42.857    0.000  977.028    0.000 agent.py:96(__call__)
                6603828   53.361    0.000  976.636    0.000 agent.py:54(modify_board)
                5677487  154.692    0.000  975.795    0.000 levels.py:95(generate)
             3634456525  647.642    0.000  920.326    0.000 enum.py:646(__hash__)
                9439538  832.581    0.000  832.581    0.000 {built-in method tensor}
               19812642  749.635    0.000  749.635    0.000 {built-in method cat}
                4402938    7.749    0.000  685.076    0.000 game.py:23(board)
              220147000   66.105    0.000  645.649    0.000 {built-in method builtins.all}
                6603828  645.186    0.000  645.186    0.000 {built-in method torch._C._nn.one_hot}
               39624126   40.454    0.000  633.037    0.000 activation.py:713(forward)
              220146900  387.370    0.000  619.510    0.000 layers.py:216(check)
              220146900  449.345    0.000  617.554    0.000 layers.py:63(check)
                2201469   46.982    0.000  607.590    0.000 replaybuffer.py:19(stacker)
              220146900  384.171    0.000  606.041    0.000 layers.py:244(check)
              686159714  171.192    0.000  605.973    0.000 layers.py:350(<genexpr>)
              220146900  371.251    0.000  599.112    0.000 layers.py:230(check)
               51097383   82.204    0.000  592.729    0.000 layer.py:48(restart)
               39624126   35.833    0.000  592.583    0.000 functional.py:1364(leaky_relu)
             1592975525  580.105    0.000  580.105    0.000 layer.py:114(elements)
               39624126  549.958    0.000  549.958    0.000 {built-in method torch._C._nn.leaky_relu}
               11354974   79.129    0.000  543.776    0.000 level.py:41(notUsed)
               79252884  541.956    0.000  541.956    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4402938   95.485    0.000  501.866    0.000 optimizer.py:189(zero_grad)
             5162188573  489.659    0.000  489.659    0.000 layer.py:67(positions)
               79252884  481.076    0.000  481.076    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              779622275  320.241    0.000  433.093    0.000 layer.py:98(add)
              220147000  290.354    0.000  411.897    0.000 layers.py:110(isDone)
              197984214  405.190    0.000  405.190    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              380452664  205.115    0.000  392.716    0.000 layer.py:94(remove)
                7878956  134.020    0.000  366.464    0.000 random.py:315(sample)
                2201469  200.175    0.000  342.509    0.000 collector.py:54(collect)
                4402359  118.876    0.000  338.369    0.000 exploration.py:53(softmaxer)
               39626442  323.283    0.000  323.283    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              220146900  208.204    0.000  312.449    0.000 layers.py:203(check)
                5677587  150.818    0.000  308.656    0.000 layers.py:33(reset)
               39626442  289.761    0.000  289.761    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              312261785  281.688    0.000  281.688    0.000 level.py:32(inverse)
             3634472764  272.688    0.000  272.688    0.000 {built-in method builtins.hash}
               39626442  264.989    0.000  264.989    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               39626442  264.188    0.000  264.188    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              277385148  193.059    0.000  241.504    0.000 tensor.py:906(grad)
                4402938   10.062    0.000  235.708    0.000 loss.py:527(forward)
                4402938   25.226    0.000  225.646    0.000 functional.py:2898(mse_loss)
        2271820963/2271820961  164.122    0.000  200.003    0.000 {built-in method builtins.len}
               39626442  189.702    0.000  189.702    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2420475471  188.429    0.000  188.429    0.000 {method 'append' of 'list' objects}
              220146900   82.153    0.000  185.298    0.000 layers.py:99(<listcomp>)
             1808695777  183.351    0.000  183.351    0.000 layer.py:175(isBlocking)
              252065251  109.288    0.000  161.159    0.000 random.py:250(_randbelow_with_getrandbits)
               13208814  152.327    0.000  152.327    0.000 {built-in method sum}
              380452664  151.936    0.000  151.936    0.000 {method 'remove' of 'list' objects}
               11354974   11.223    0.000  139.531    0.000 level.py:38(elementsIn)
                2201469   12.412    0.000  139.014    0.000 exploration.py:47(epsilonGreedy)
                4402938  131.895    0.000  131.895    0.000 {built-in method torch._C._nn.mse_loss}
                6604407   14.927    0.000  119.480    0.000 tensor.py:525(__rsub__)
                4403598  119.098    0.000  119.098    0.000 {built-in method max}
               22013532   17.911    0.000  109.018    0.000 flatten.py:39(forward)
                4402359  108.544    0.000  108.544    0.000 {built-in method multinomial}
                6604407  102.868    0.000  102.868    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9441982: <Rock_level_Khigh_0> in cluster <dcc> Done

Job <Rock_level_Khigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:11 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:12 2021
Terminated at Sat Mar 20 13:08:39 2021
Results reported at Sat Mar 20 13:08:39 2021

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

    CPU time :                                   42801.63 sec.
    Max Memory :                                 5418 MB
    Average Memory :                             4075.59 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2774.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42965 sec.
    Turnaround time :                            42928 sec.

The output (if any) is above this job summary.

