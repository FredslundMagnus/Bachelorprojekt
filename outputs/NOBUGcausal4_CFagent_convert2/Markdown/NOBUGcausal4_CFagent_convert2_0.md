
# Parameters

    Name :                      NOBUGcausal4_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      38056155092 function calls (37843158897 primitive calls) in 57317.80 seconds

##    Ordered by: cumulative time
   List reduced from 492 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57317.804 57317.804 {built-in method builtins.exec}
                      1    4.653    4.653 57317.804 57317.804 <string>:1(<module>)
                      1  174.530  174.530 57313.151 57313.151 main.py:96(CFagent)
                7139457   26.858    0.000 21326.989    0.003 agent.py:28(learn)
                7139450  531.789    0.000 17727.073    0.002 learner.py:42(Qlearn)
                2379819   12.248    0.000 11453.866    0.005 game.py:36(step)
                2379819   14.587    0.000 10861.304    0.005 layers.py:594(step)
        238676769/25682265  981.889    0.000 8814.573    0.000 module.py:866(_call_impl)
               18542815   50.150    0.000 8255.994    0.000 network.py:24(forward)
                2379819  261.196    0.000 8244.700    0.003 agent.py:53(_learn)
               18542815  264.648    0.000 8083.256    0.000 container.py:117(forward)
                2379819  258.290    0.000 7634.075    0.003 agent.py:191(_learn)
                2379819  206.857    0.000 7565.229    0.003 layers.py:18(step)
                7139450   58.785    0.000 7479.834    0.001 optimizer.py:84(wrapper)
              236975217  492.241    0.000 7338.955    0.000 layer.py:82(move)
                7139450   29.834    0.000 7189.689    0.001 grad_mode.py:24(decorate_context)
                7139450  215.872    0.000 7093.106    0.001 adam.py:55(step)
                2379819  690.167    0.000 6868.020    0.003 agent.py:199(counterfact)
                7139450 1466.196    0.000 6648.346    0.001 _functional.py:53(adam)
                2379819   72.451    0.000 5406.118    0.002 agent.py:114(_learn)
                7139450   29.975    0.000 4442.454    0.001 tensor.py:195(backward)
              236975217  698.944    0.000 4434.084    0.000 layers.py:611(check)
                7139450   27.401    0.000 4411.437    0.001 __init__.py:68(backward)
                7139450 4225.707    0.001 4225.707    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5697237  158.109    0.000 4132.255    0.001 agent.py:48(__call__)
               37514839 3971.717    0.000 3971.717    0.000 {built-in method tensor}
               31945769   20.503    0.000 3807.585    0.000 game.py:32(board)
                2379819 2772.951    0.001 3664.887    0.002 replaybuffer.py:22(sample_data)
                2379819 1754.487    0.001 3290.585    0.001 replaybuffer.py:28(teleporter_save_data)
                2379820  255.224    0.000 3259.455    0.001 layers.py:565(update)
                2379819 1415.642    0.001 3125.605    0.001 agent.py:85(interveen)
                2379819 2287.336    0.001 3063.118    0.001 replaybuffer.py:49(sample_data)
               47596390 1717.500    0.000 2976.095    0.000 layer.py:127(update)
               37085630   84.349    0.000 2923.677    0.000 conv.py:398(forward)
               37085630   52.473    0.000 2800.628    0.000 conv.py:390(_conv_forward)
               37085630 2748.155    0.000 2748.155    0.000 {built-in method conv2d}
               50868807  103.357    0.000 2338.870    0.000 linear.py:93(forward)
               50868807   41.485    0.000 2183.125    0.000 functional.py:1737(linear)
               50868807 2131.202    0.000 2131.202    0.000 {built-in method torch._C._nn.linear}
              236486792  374.974    0.000 2121.440    0.000 layers.py:605(isFree)
                2379819 1097.442    0.000 1835.024    0.001 agent.py:66(modify)
             1757367421 1478.147    0.000 1746.466    0.000 layer.py:79(isFree)
              111237463 1469.767    0.000 1469.767    0.000 {built-in method clone}
               34255030 1435.681    0.000 1435.681    0.000 {built-in method cat}
              133269724 1360.693    0.000 1360.693    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               69411622   58.271    0.000 1297.912    0.000 activation.py:713(forward)
               69411622   58.830    0.000 1239.641    0.000 functional.py:1364(leaky_relu)
                2379812   45.777    0.000 1202.379    0.001 agent.py:163(__call__)
              133269724 1190.105    0.000 1190.105    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               69411622 1168.177    0.000 1168.177    0.000 {built-in method torch._C._nn.leaky_relu}
                8077056   54.412    0.000 1163.294    0.000 agent.py:58(modify_board)
                 946497    9.618    0.000 1138.126    0.001 agent.py:167(choose_action)
                2379819   43.900    0.000 1136.242    0.000 agent.py:109(__call__)
                7139450  167.081    0.000 1039.463    0.000 optimizer.py:189(zero_grad)
             3883637716  640.831    0.000  901.021    0.000 enum.py:646(__hash__)
                2441445   25.654    0.000  794.822    0.000 layers.py:615(restart)
              236975217  500.875    0.000  763.316    0.000 layers.py:303(check)
                8077056  740.850    0.000  740.850    0.000 {built-in method torch._C._nn.one_hot}
              767516042  736.179    0.000  736.179    0.000 layer.py:122(elements)
               66634862  733.424    0.000  733.424    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2379819   58.114    0.000  723.650    0.000 replaybuffer.py:18(stacker)
              236975217  417.016    0.000  676.518    0.000 layers.py:262(check)
               66634862  648.872    0.000  648.872    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              236975217  500.563    0.000  641.999    0.000 layers.py:76(check)
               66634862  619.491    0.000  619.491    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2379812   54.484    0.000  614.705    0.000 replaybuffer.py:45(stacker)
              237982000   63.786    0.000  613.030    0.000 {built-in method builtins.all}
               66634862  608.747    0.000  608.747    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2379819  243.242    0.000  600.663    0.000 replaybuffer.py:55(CF_save_data)
              733481575  168.779    0.000  576.201    0.000 layers.py:571(<genexpr>)
                2441445   13.457    0.000  542.279    0.000 level.py:8(__init__)
              236975217  419.128    0.000  516.949    0.000 layers.py:63(check)
                2379819  294.706    0.000  485.683    0.000 collector.py:54(collect)
             5643731945  481.348    0.000  481.348    0.000 layer.py:75(positions)
               66634862  473.470    0.000  473.470    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2441445   98.044    0.000  455.330    0.000 levels.py:199(generate)
                5697237  153.603    0.000  430.377    0.000 exploration.py:53(softmaxer)
              236975217  260.269    0.000  394.397    0.000 layers.py:329(check)
              237982000  264.449    0.000  384.798    0.000 layers.py:111(isDone)
              466444118  310.772    0.000  383.492    0.000 tensor.py:906(grad)
        5239594586/5239594583  331.073    0.000  376.179    0.000 {built-in method builtins.len}
              121694331  371.674    0.000  371.674    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              236975217  241.830    0.000  369.214    0.000 layers.py:288(check)
                9642528  131.240    0.000  350.550    0.000 random.py:315(sample)
                7139450   11.847    0.000  345.133    0.000 loss.py:527(forward)
                7139450   26.503    0.000  333.286    0.000 functional.py:2898(mse_loss)
                7139458  315.278    0.000  315.278    0.000 {built-in method nonzero}
              236975217  216.379    0.000  312.908    0.000 layers.py:47(check)
                4882890   32.568    0.000  288.823    0.000 level.py:41(notUsed)
             3883664963  260.194    0.000  260.194    0.000 {built-in method builtins.hash}
                7139450  219.987    0.000  219.987    0.000 {built-in method torch._C._nn.mse_loss}
               24414450   30.324    0.000  219.434    0.000 layer.py:56(restart)
               37085630   25.146    0.000  212.651    0.000 flatten.py:39(forward)
               14278914  204.199    0.000  204.199    0.000 {built-in method sum}
                7140256  197.591    0.000  197.591    0.000 {built-in method max}
              180932525  140.250    0.000  192.847    0.000 layer.py:102(remove)
               47596390  189.337    0.000  189.337    0.000 layer.py:139(<listcomp>)
               37085630  187.505    0.000  187.505    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              336428710  130.240    0.000  179.513    0.000 layer.py:106(add)
                9519269   13.339    0.000  174.474    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9494243: <NOBUGcausal4_CFagent_convert2_0> in cluster <dcc> Done

Job <NOBUGcausal4_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 18:55:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 18:55:27 2021
Terminated at Mon Apr  5 10:50:58 2021
Results reported at Mon Apr  5 10:50:58 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   57165.82 sec.
    Max Memory :                                 7751 MB
    Average Memory :                             5493.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8633.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57332 sec.
    Turnaround time :                            114665 sec.

The output (if any) is above this job summary.

