
# Parameters

    Name :                      Rock_level_hard_Klow-0
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
    K :                         10000.0
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


      32757927060 function calls (32641497369 primitive calls) in 39314.62 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39314.620 39314.620 {built-in method builtins.exec}
                      1    0.964    0.964 39314.620 39314.620 <string>:1(<module>)
                      1   91.701   91.701 39313.656 39313.656 main.py:13(teleport)
                2079093    8.406    0.000 13529.809    0.007 game.py:27(step)
                2079093   10.623    0.000 13040.806    0.006 layers.py:373(step)
                4158186   14.951    0.000 11543.373    0.003 agent.py:26(learn)
                4158186  306.168    0.000 9897.418    0.002 learner.py:42(Qlearn)
                2079093  160.190    0.000 8885.015    0.004 layers.py:18(step)
              207909300  397.870    0.000 8707.554    0.000 layer.py:74(move)
                2079093   69.007    0.000 6874.807    0.003 agent.py:50(_learn)
              207909300  616.666    0.000 6741.365    0.000 layers.py:390(check)
                2079093 3127.533    0.002 5676.607    0.003 replaybuffer.py:27(teleporter_save_data)
        130982287/14553607  529.306    0.000 4753.448    0.000 module.py:866(_call_impl)
                2079093   61.628    0.000 4645.251    0.002 agent.py:101(_learn)
               10395421   29.445    0.000 4427.891    0.000 network.py:24(forward)
               10395421  141.408    0.000 4335.268    0.000 container.py:117(forward)
                4158186   34.896    0.000 4145.369    0.001 optimizer.py:84(wrapper)
                2079094  211.278    0.000 4132.169    0.002 layers.py:344(update)
                4158186   16.892    0.000 3977.311    0.001 grad_mode.py:24(decorate_context)
                4158186  114.603    0.000 3922.761    0.001 adam.py:55(step)
              207909300 3477.989    0.000 3880.444    0.000 layers.py:76(check)
                2079093 2353.136    0.001 3808.150    0.002 agent.py:77(interveen)
                4158186  810.171    0.000 3673.000    0.001 _functional.py:53(adam)
                4158142   95.267    0.000 2934.776    0.001 agent.py:45(__call__)
                4158186   17.241    0.000 2447.972    0.001 tensor.py:195(backward)
                4158186   16.728    0.000 2430.138    0.001 __init__.py:68(backward)
                4158186 2324.424    0.001 2324.424    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              174942492 2046.551    0.000 2046.551    0.000 {built-in method clone}
                6246727   54.573    0.000 1727.572    0.000 layers.py:394(restart)
                2079093 1016.860    0.000 1635.186    0.001 agent.py:59(modify)
               18711846 1059.312    0.000 1602.651    0.000 layer.py:119(update)
               20790842   45.714    0.000 1581.739    0.000 conv.py:398(forward)
               20790842   26.067    0.000 1517.628    0.000 conv.py:390(_conv_forward)
               20790842 1491.561    0.000 1491.561    0.000 {built-in method conv2d}
                2079093  718.752    0.000 1442.472    0.001 replaybuffer.py:23(sample_data)
              207909300  323.415    0.000 1414.477    0.000 layers.py:384(isFree)
               27028077   56.622    0.000 1230.995    0.000 linear.py:93(forward)
               27028077   22.876    0.000 1150.911    0.000 functional.py:1737(linear)
               27028077 1122.493    0.000 1122.493    0.000 {built-in method torch._C._nn.linear}
                6246727   25.334    0.000 1101.462    0.000 level.py:8(__init__)
             1526954387  904.727    0.000 1091.062    0.000 layer.py:71(isFree)
                6246727  158.946    0.000  986.811    0.000 levels.py:95(generate)
                2079093   29.400    0.000  899.788    0.000 agent.py:96(__call__)
                6237235   40.919    0.000  897.824    0.000 agent.py:54(modify_board)
             3517521578  575.861    0.000  829.047    0.000 enum.py:646(__hash__)
               74847348  744.550    0.000  744.550    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18711793  733.666    0.000  733.666    0.000 {built-in method cat}
               37423498   28.965    0.000  696.138    0.000 activation.py:713(forward)
                8535780  679.202    0.000  679.202    0.000 {built-in method tensor}
               37423498   31.524    0.000  667.174    0.000 functional.py:1364(leaky_relu)
               74847348  662.765    0.000  662.765    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               37423498  628.941    0.000  628.941    0.000 {built-in method torch._C._nn.leaky_relu}
                4158186   95.558    0.000  591.157    0.000 optimizer.py:189(zero_grad)
                2079093   37.442    0.000  582.712    0.000 replaybuffer.py:19(stacker)
                6237235  576.536    0.000  576.536    0.000 {built-in method torch._C._nn.one_hot}
              181179727  563.671    0.000  563.671    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               56220543   76.333    0.000  554.971    0.000 layer.py:48(restart)
                4158186    4.780    0.000  548.612    0.000 game.py:23(board)
               12493454   71.315    0.000  538.844    0.000 level.py:41(notUsed)
              207909300  316.282    0.000  515.909    0.000 layers.py:216(check)
              207909300  314.957    0.000  515.437    0.000 layers.py:230(check)
              207909300  314.202    0.000  512.486    0.000 layers.py:244(check)
              207909400   55.325    0.000  508.496    0.000 {built-in method builtins.all}
              623845359  141.327    0.000  477.530    0.000 layers.py:350(<genexpr>)
             4824144976  421.370    0.000  421.370    0.000 layer.py:67(positions)
                2079093  249.181    0.000  414.753    0.000 collector.py:54(collect)
               37423674  409.877    0.000  409.877    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              207909300  270.015    0.000  393.165    0.000 layers.py:63(check)
               37423674  355.887    0.000  355.887    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1510069682  355.843    0.000  355.843    0.000 layer.py:114(elements)
              736673721  259.915    0.000  349.127    0.000 layer.py:98(add)
               37423674  342.903    0.000  342.903    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37423674  336.298    0.000  336.298    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8325820  118.158    0.000  333.570    0.000 random.py:315(sample)
              207909400  209.192    0.000  318.495    0.000 layers.py:110(isDone)
                4158142  111.459    0.000  304.217    0.000 exploration.py:53(softmaxer)
                6246827  149.564    0.000  303.657    0.000 layers.py:33(reset)
              312336350  283.745    0.000  283.745    0.000 level.py:32(inverse)
               37423674  262.776    0.000  262.776    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              207909300  164.812    0.000  255.064    0.000 layers.py:203(check)
             3517536881  253.189    0.000  253.189    0.000 {built-in method builtins.hash}
              271956658  120.492    0.000  247.482    0.000 layer.py:94(remove)
              261965772  186.091    0.000  228.522    0.000 tensor.py:906(grad)
                4158186    6.675    0.000  201.008    0.000 loss.py:527(forward)
                4158186   15.166    0.000  194.333    0.000 functional.py:2898(mse_loss)
        2231591985/2231591983  154.329    0.000  186.050    0.000 {built-in method builtins.len}
               12474558  174.748    0.000  174.748    0.000 {built-in method sum}
              291408045  112.198    0.000  161.876    0.000 random.py:250(_randbelow_with_getrandbits)
             2242713846  147.605    0.000  147.605    0.000 {method 'append' of 'list' objects}
             1526954387  140.765    0.000  140.765    0.000 layer.py:175(isBlocking)
               12493454   10.261    0.000  140.716    0.000 level.py:38(elementsIn)
              207909300   62.473    0.000  136.552    0.000 layers.py:99(<listcomp>)
                4158186  127.325    0.000  127.325    0.000 {built-in method torch._C._nn.mse_loss}
               20790842   14.773    0.000  120.088    0.000 flatten.py:39(forward)
                4158808  112.530    0.000  112.530    0.000 {built-in method max}
                6237279    9.075    0.000  112.391    0.000 tensor.py:525(__rsub__)
               20790842  105.315    0.000  105.315    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              271956658  105.136    0.000  105.136    0.000 {method 'remove' of 'list' objects}
                6237279  101.702    0.000  101.702    0.000 {built-in method rsub}
                4158142   96.434    0.000   96.434    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9444622: <Rock_level_hard_Klow_0> in cluster <dcc> Done

Job <Rock_level_hard_Klow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:57 2021
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

    CPU time :                                   39209.77 sec.
    Max Memory :                                 5307 MB
    Average Memory :                             3884.04 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2885.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39355 sec.
    Turnaround time :                            39327 sec.

The output (if any) is above this job summary.

