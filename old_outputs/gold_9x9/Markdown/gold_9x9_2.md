
# Parameters

    Name :                      gold_9x9-2
    Main :                      teleport
    Hours :                     24.0
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
    Layer keys :                False
    Layer door :                False
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      47642801005 function calls (47367700846 primitive calls) in 85997.99 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.104 86112.104 {built-in method builtins.exec}
                      1    0.781    0.781 86112.104 86112.104 <string>:1(<module>)
                      1  195.317  195.317 86111.323 86111.323 main.py:10(teleport)
                9825120   37.122    0.000 32144.559    0.003 agent.py:26(learn)
                9825120  763.862    0.000 27896.353    0.003 learner.py:42(Qlearn)
                4912560  142.877    0.000 19127.362    0.004 agent.py:50(_learn)
                4912560 8546.867    0.002 16098.716    0.003 replaybuffer.py:27(teleporter_save_data)
                4912560   18.970    0.000 13284.442    0.003 game.py:25(step)
                4912560  126.614    0.000 12961.912    0.003 agent.py:101(_learn)
        309486717/34387569 1170.765    0.000 12671.294    0.000 module.py:715(_call_impl)
                4912560   23.588    0.000 12318.182    0.003 layers.py:295(step)
                4912560 8268.228    0.002 12133.550    0.002 agent.py:77(interveen)
                9825120   56.470    0.000 11894.249    0.001 grad_mode.py:23(decorate_context)
               24562449   64.185    0.000 11863.610    0.000 network.py:24(forward)
                9825120  303.249    0.000 11733.096    0.001 adam.py:55(step)
               24562449  297.269    0.000 11662.846    0.000 container.py:115(forward)
                9825120 2131.998    0.000 10050.851    0.001 functional.py:53(adam)
                9824769  196.506    0.000 7734.565    0.001 agent.py:45(__call__)
                4912561  480.330    0.000 7525.614    0.002 layers.py:266(update)
                9825120   58.660    0.000 6337.756    0.001 tensor.py:181(backward)
                9825120   32.938    0.000 6279.096    0.001 __init__.py:68(backward)
                9825120 6003.410    0.001 6003.410    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              447397795 5832.099    0.000 5832.099    0.000 {built-in method clone}
                4912560  333.541    0.000 4740.299    0.001 layers.py:19(step)
                4912560 2308.338    0.000 4556.980    0.001 agent.py:59(modify)
              491256000  530.114    0.000 4367.126    0.000 layer.py:70(move)
               49124898   81.980    0.000 4210.368    0.000 conv.py:422(forward)
               49124898   92.726    0.000 4098.393    0.000 conv.py:414(_conv_forward)
               10352606   81.457    0.000 4059.292    0.000 layers.py:316(restart)
               49124898 3990.275    0.000 3990.275    0.000 {built-in method conv2d}
               63862227  141.312    0.000 3816.202    0.000 linear.py:92(forward)
                4912560 1574.312    0.000 3753.899    0.001 replaybuffer.py:23(sample_data)
               63862227  243.807    0.000 3614.891    0.000 functional.py:1669(linear)
               10352606   14.011    0.000 3243.167    0.000 levels.py:8(__init__)
               10352606   38.267    0.000 3229.156    0.000 level.py:8(__init__)
               10352606  532.272    0.000 3081.275    0.000 levels.py:11(generate)
               63862227 2588.915    0.000 2588.915    0.000 {built-in method addmm}
              618982614 1659.160    0.000 2578.291    0.000 tensor.py:933(grad)
                9825120  235.371    0.000 2478.163    0.000 optimizer.py:167(zero_grad)
                4912560   61.140    0.000 2421.840    0.000 agent.py:96(__call__)
               14737329  100.177    0.000 2341.399    0.000 agent.py:54(modify_board)
               39300129 2291.839    0.000 2291.839    0.000 {built-in method cat}
              176852160 2106.213    0.000 2106.213    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              491256000  380.772    0.000 2011.277    0.000 layers.py:306(isFree)
              462135124 1857.952    0.000 1857.952    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4912560   80.471    0.000 1849.912    0.000 replaybuffer.py:19(stacker)
              176852160 1789.642    0.000 1789.642    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               88424676   74.519    0.000 1732.767    0.000 activation.py:713(forward)
               88424676  108.030    0.000 1658.248    0.000 functional.py:1292(leaky_relu)
             1778944737 1383.602    0.000 1630.505    0.000 layer.py:67(isFree)
               19650244  970.798    0.000 1583.583    0.000 layer.py:132(NoRock_update)
               88424676 1539.695    0.000 1539.695    0.000 {built-in method torch._C._nn.leaky_relu}
               14737329 1466.816    0.000 1466.816    0.000 {built-in method torch._C._nn.one_hot}
              491256000  497.993    0.000 1326.284    0.000 layers.py:312(check)
               10352606  675.214    0.000 1298.806    0.000 levels.py:77(RFS)
              510908404  146.719    0.000 1243.050    0.000 {built-in method builtins.all}
               20714071 1227.568    0.000 1227.568    0.000 {built-in method tensor}
              790922333  411.685    0.000 1207.781    0.000 overrides.py:1070(has_torch_function)
               88426080 1149.532    0.000 1149.532    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1494314646  333.312    0.000 1137.386    0.000 layers.py:272(<genexpr>)
                4912560  660.418    0.000 1105.540    0.000 collector.py:37(collect)
               88426080 1027.566    0.000 1027.566    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               88426080  966.123    0.000  966.123    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9825120   10.973    0.000  878.083    0.000 game.py:21(board)
               88426080  852.911    0.000  852.911    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9824769  296.119    0.000  826.078    0.000 exploration.py:53(softmaxer)
              491256100  501.595    0.000  759.482    0.000 layers.py:111(isDone)
              874434801  310.473    0.000  756.338    0.000 {built-in method builtins.any}
               41410424   73.205    0.000  719.140    0.000 layer.py:44(restart)
              491256000  463.492    0.000  715.728    0.000 layers.py:48(check)
               88426080  689.507    0.000  689.507    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               19652304   90.194    0.000  586.969    0.000 tensor.py:21(wrapped)
                9825120   13.235    0.000  534.342    0.000 loss.py:445(forward)
                9825120   52.878    0.000  521.106    0.000 functional.py:2637(mse_loss)
               63862227  502.147    0.000  502.147    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10352706  247.236    0.000  488.974    0.000 layers.py:34(reset)
              998626109  355.075    0.000  486.128    0.000 layer.py:94(add)
               25617772  185.118    0.000  474.410    0.000 random.py:315(sample)
             1624373676  312.823    0.000  444.300    0.000 enum.py:646(__hash__)
               29475360  442.695    0.000  442.695    0.000 {built-in method sum}
             1665358215  349.782    0.000  439.699    0.000 overrides.py:1083(<genexpr>)
               10352606   66.509    0.000  424.521    0.000 level.py:41(notUsed)
             2026987358  397.497    0.000  397.497    0.000 layer.py:110(elements)
        2898132008/2898132006  241.581    0.000  381.464    0.000 {built-in method builtins.len}
               14737680   68.573    0.000  345.144    0.000 tensor.py:506(__rsub__)
             3878374385  326.921    0.000  326.921    0.000 layer.py:63(positions)
                9825120  325.029    0.000  325.029    0.000 {built-in method torch._C._nn.mse_loss}
               49124898   32.711    0.000  323.652    0.000 flatten.py:39(forward)
              507277694  312.375    0.000  312.375    0.000 level.py:32(inverse)
               14737680  306.234    0.000  306.234    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              464290139  208.536    0.000  303.448    0.000 random.py:250(_randbelow_with_getrandbits)
              621156360  201.102    0.000  302.947    0.000 levels.py:33(<genexpr>)
                9826593  294.509    0.000  294.509    0.000 {built-in method max}
              457910787  193.857    0.000  291.764    0.000 layer.py:90(remove)
               49124898  290.941    0.000  290.941    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14737680  276.571    0.000  276.571    0.000 {built-in method rsub}
              314401241  275.067    0.000  275.067    0.000 {built-in method torch._C._get_tracing_state}
                9824769  268.379    0.000  268.379    0.000 {built-in method multinomial}
             3310973306  242.286    0.000  242.286    0.000 {method 'append' of 'list' objects}
                9825120  241.386    0.000  241.386    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9418587: <gold_9x9_2> in cluster <dcc> Done

Job <gold_9x9_2> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Mar 16 21:35:11 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar 16 21:35:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 16 21:35:12 2021
Terminated at Wed Mar 17 21:30:36 2021
Results reported at Wed Mar 17 21:30:36 2021

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

    CPU time :                                   85894.25 sec.
    Max Memory :                                 2390 MB
    Average Memory :                             2385.95 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5802.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86140 sec.
    Turnaround time :                            86125 sec.

The output (if any) is above this job summary.

