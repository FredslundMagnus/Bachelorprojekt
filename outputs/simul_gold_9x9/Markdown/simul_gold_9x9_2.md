
# Parameters

    Name :                      simul_gold_9x9-2
    Main :                      simulation
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
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      9061825145 function calls (9026992132 primitive calls) in 14076.53 seconds

##    Ordered by: cumulative time
   List reduced from 449 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14103.990 14103.990 {built-in method builtins.exec}
                      1    0.912    0.912 14103.990 14103.990 <string>:1(<module>)
                      1   39.592   39.592 14103.078 14103.078 main.py:47(simulation)
                 967559   24.167    0.000 3670.638    0.004 simulator.py:51(learn)
                 967559  210.539    0.000 3646.470    0.004 simulator.py:28(learn)
                 967559 1760.934    0.002 3137.759    0.003 replaybuffer.py:27(teleporter_save_data)
                 967559    3.450    0.000 3012.204    0.003 game.py:27(step)
                 967559    5.056    0.000 2833.905    0.003 layers.py:295(step)
                 967559 1352.705    0.001 2071.668    0.002 agent.py:77(interveen)
                 967559  103.550    0.000 1801.072    0.002 layers.py:266(update)
        40637283/5805339  157.005    0.000 1590.810    0.000 module.py:715(_call_impl)
                3870221   39.799    0.000 1426.616    0.000 container.py:115(forward)
                1935118   10.947    0.000 1311.410    0.001 grad_mode.py:23(decorate_context)
                1935118   47.634    0.000 1279.322    0.001 adam.py:55(step)
              106856782 1085.930    0.000 1085.930    0.000 {built-in method clone}
                1935118  235.466    0.000 1042.552    0.001 functional.py:53(adam)
                2424241   20.549    0.000 1028.682    0.000 layers.py:316(restart)
                 967559   71.692    0.000 1021.389    0.001 layers.py:18(step)
               96755900  111.938    0.000  941.025    0.000 layer.py:70(move)
                1935103    4.758    0.000  839.804    0.000 network.py:24(forward)
                 967559  344.280    0.000  825.432    0.001 replaybuffer.py:23(sample_data)
                2424241    9.316    0.000  819.344    0.000 level.py:8(__init__)
                 967559  409.496    0.000  814.160    0.001 agent.py:59(modify)
                2424241  137.902    0.000  782.143    0.000 levels.py:9(generate)
                1935118   10.952    0.000  771.430    0.000 tensor.py:181(backward)
                1935118    6.263    0.000  760.478    0.000 __init__.py:68(backward)
                1935118  710.082    0.000  710.082    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 967544   25.257    0.000  705.722    0.001 agent.py:45(__call__)
                7740442   13.117    0.000  603.472    0.000 conv.py:422(forward)
                7740442   15.534    0.000  585.266    0.000 conv.py:414(_conv_forward)
                7740442  566.902    0.000  566.902    0.000 {built-in method conv2d}
                9675575  514.519    0.000  514.519    0.000 {built-in method cat}
                 967559   19.168    0.000  451.539    0.000 agent.py:96(__call__)
               96755900   85.618    0.000  433.179    0.000 layers.py:306(isFree)
                 967559   17.101    0.000  411.468    0.000 replaybuffer.py:19(stacker)
                6772868   16.736    0.000  376.500    0.000 linear.py:92(forward)
                3870236  223.681    0.000  362.508    0.000 layer.py:132(NoRock_update)
                6772868   26.889    0.000  352.375    0.000 functional.py:1669(linear)
              356265623  293.840    0.000  347.560    0.000 layer.py:67(isFree)
               81274968  202.980    0.000  338.702    0.000 tensor.py:933(grad)
                2424241  168.689    0.000  323.619    0.000 levels.py:75(RFS)
                 967559    3.257    0.000  316.554    0.000 simulator.py:25(RDforward)
                 967559    3.382    0.000  310.623    0.000 simulator.py:22(boardforward)
              109759444  307.176    0.000  307.176    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1935118   28.784    0.000  296.039    0.000 optimizer.py:167(zero_grad)
               96755900  106.333    0.000  284.379    0.000 layers.py:312(check)
                1935103   13.474    0.000  282.250    0.000 agent.py:54(modify_board)
              102561446   33.435    0.000  274.615    0.000 {built-in method builtins.all}
                2902662  268.819    0.000  268.819    0.000 {built-in method torch._C._nn.one_hot}
                6772868  250.606    0.000  250.606    0.000 {built-in method addmm}
              294964490   74.338    0.000  248.780    0.000 layers.py:272(<genexpr>)
                4063766  224.718    0.000  224.718    0.000 {built-in method tensor}
               23221416  211.698    0.000  211.698    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11610648   11.877    0.000  200.552    0.000 activation.py:713(forward)
               11610648   15.991    0.000  188.675    0.000 functional.py:1292(leaky_relu)
                9696964   18.133    0.000  184.864    0.000 layer.py:44(restart)
              105464072   60.780    0.000  183.153    0.000 overrides.py:1070(has_torch_function)
               23221416  173.896    0.000  173.896    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5805546   31.823    0.000  171.736    0.000 tensor.py:21(wrapped)
               11610648  170.982    0.000  170.982    0.000 {built-in method torch._C._nn.leaky_relu}
               96755900  108.843    0.000  164.677    0.000 layers.py:110(isDone)
                1935118    2.103    0.000  163.583    0.000 game.py:23(board)
               96755900   98.836    0.000  154.038    0.000 layers.py:47(check)
                2424241   64.055    0.000  126.900    0.000 layers.py:33(reset)
               11610708  124.644    0.000  124.644    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              219836496   85.802    0.000  117.719    0.000 layer.py:94(add)
              116107177   46.936    0.000  115.794    0.000 {built-in method builtins.any}
               11610708  109.588    0.000  109.588    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2424241   16.860    0.000  109.114    0.000 level.py:41(notUsed)
                5816041   41.861    0.000  106.131    0.000 random.py:315(sample)
                1935118    2.653    0.000  103.162    0.000 loss.py:445(forward)
              343814756   71.613    0.000  101.922    0.000 enum.py:646(__hash__)
                1935118   10.357    0.000  100.509    0.000 functional.py:2637(mse_loss)
               11610708   98.420    0.000   98.420    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              445084224   91.844    0.000   91.844    0.000 layer.py:110(elements)
                4837795   91.255    0.000   91.255    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               11610708   85.227    0.000   85.227    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              118787809   81.244    0.000   81.244    0.000 level.py:32(inverse)
              145454460   52.007    0.000   78.106    0.000 levels.py:31(<genexpr>)
                 967544   26.798    0.000   72.512    0.000 exploration.py:53(softmaxer)
              766218782   72.135    0.000   72.135    0.000 layer.py:63(positions)
               99577394   48.664    0.000   70.758    0.000 random.py:250(_randbelow_with_getrandbits)
               11610708   69.944    0.000   69.944    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              223506462   53.759    0.000   67.479    0.000 overrides.py:1083(<genexpr>)
               93431150   44.365    0.000   66.402    0.000 layer.py:90(remove)
                1935118   64.299    0.000   64.299    0.000 {built-in method torch._C._nn.mse_loss}
        522442713/522442712   41.004    0.000   56.768    0.000 {built-in method builtins.len}
              687641235   55.064    0.000   55.064    0.000 {method 'append' of 'list' objects}
               38787856   18.466    0.000   52.398    0.000 random.py:285(choice)
                2902677   44.889    0.000   44.889    0.000 {built-in method sum}
                6772868   43.365    0.000   43.365    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1935118    8.021    0.000   42.283    0.000 __init__.py:28(_make_grads)
                7740442   41.775    0.000   41.775    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 967559    3.479    0.000   41.122    0.000 exploration.py:47(epsilonGreedy)
                6772883    5.225    0.000   40.288    0.000 flatten.py:39(forward)
              237468193   39.217    0.000   39.217    0.000 {method 'add' of 'set' objects}
              356265623   36.846    0.000   36.846    0.000 layer.py:172(isBlocking)
                1942894   33.509    0.000   33.509    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               11610786   14.699    0.000   33.388    0.000 tensor.py:596(__hash__)
               41605034   33.036    0.000   33.036    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9434613: <simul_gold_9x9_2> in cluster <dcc> Done

Job <simul_gold_9x9_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:53:09 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:53:09 2021
Terminated at Fri Mar 19 00:48:15 2021
Results reported at Fri Mar 19 00:48:15 2021

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

    CPU time :                                   14071.05 sec.
    Max Memory :                                 2435 MB
    Average Memory :                             2431.77 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5757.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14107 sec.
    Turnaround time :                            16308 sec.

The output (if any) is above this job summary.

