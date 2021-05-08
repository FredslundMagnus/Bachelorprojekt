
# Parameters

    Name :                      Causal4_Conver4_3counterfacts_2-0
    Main :                      Load_Cfagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55390375824 function calls (55087427315 primitive calls) in 86112.81 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.809 86112.809 {built-in method builtins.exec}
                      1    6.732    6.732 86112.809 86112.809 <string>:1(<module>)
                      1  357.831  357.831 86106.077 86106.077 main.py:109(Load_Cfagent)
                2193846 2991.316    0.001 25810.214    0.012 agent.py:212(counterfact)
                6581538   32.436    0.000 17787.042    0.003 agent.py:29(learn)
                2193846   13.870    0.000 16041.344    0.007 game.py:42(step)
                2193846   16.022    0.000 15484.082    0.007 layers.py:827(step)
                6581538  457.349    0.000 14247.237    0.002 learner.py:42(Qlearn)
        335503982/32558294 1516.102    0.000 11705.206    0.000 module.py:866(_call_impl)
               25976756   74.076    0.000 11055.556    0.000 network.py:28(forward)
               25976756  350.650    0.000 10782.334    0.000 container.py:117(forward)
               92613853 10366.255    0.000 10366.255    0.000 {built-in method tensor}
               87775065   59.932    0.000 10278.314    0.000 game.py:38(board)
                2193846  222.559    0.000 9716.081    0.004 layers.py:17(step)
              219327876  684.467    0.000 9473.732    0.000 layer.py:106(move)
                5313421  112.417    0.000 7694.644    0.001 agent.py:176(choose_action)
                2193846 6588.023    0.003 7556.046    0.003 replaybuffer.py:22(sample_data)
                2193846 6451.972    0.003 7365.233    0.003 replaybuffer.py:67(sample_data)
                2193846  325.671    0.000 6939.035    0.003 agent.py:54(_learn)
                9694105  330.259    0.000 6692.062    0.001 agent.py:49(__call__)
               87753820 3620.626    0.000 6428.295    0.000 layer.py:159(update)
                2193846  323.982    0.000 6312.991    0.003 agent.py:204(_learn)
                2193846  346.179    0.000 5726.135    0.003 layers.py:793(update)
              219327876 1080.031    0.000 5683.933    0.000 layers.py:844(check)
                6581538   75.256    0.000 5368.843    0.001 optimizer.py:84(wrapper)
                6581538   38.895    0.000 5081.138    0.001 grad_mode.py:24(decorate_context)
                6581538  238.185    0.000 4961.106    0.001 adam.py:55(step)
                2193846   83.485    0.000 4485.743    0.002 agent.py:117(_learn)
                6581538 1036.415    0.000 4482.758    0.001 _functional.py:53(adam)
               51953512  121.695    0.000 3964.805    0.000 conv.py:398(forward)
                6581538   28.200    0.000 3825.216    0.001 tensor.py:195(backward)
                6581538   36.055    0.000 3796.047    0.001 __init__.py:68(backward)
               51953512   95.914    0.000 3772.973    0.000 conv.py:390(_conv_forward)
               51953512 3677.059    0.000 3677.059    0.000 {built-in method conv2d}
                6581538 3614.216    0.001 3614.216    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2193846 1967.027    0.001 3308.849    0.002 replaybuffer.py:28(teleporter_save_data)
                2193846 1583.552    0.001 3075.723    0.001 agent.py:88(interveen)
               73542576  151.929    0.000 3038.828    0.000 linear.py:93(forward)
               73542576   64.159    0.000 2793.005    0.000 functional.py:1737(linear)
               73542576 2715.144    0.000 2715.144    0.000 {built-in method torch._C._nn.linear}
              219327876  472.697    0.000 2639.190    0.000 layers.py:838(isFree)
             2075090745 1827.808    0.000 2166.494    0.000 layer.py:103(isFree)
                2193846 1204.195    0.001 1802.889    0.001 agent.py:67(modify)
               33826411 1708.485    0.000 1708.485    0.000 {built-in method cat}
                4086165   63.393    0.000 1690.898    0.000 layers.py:849(restart)
             1119189377 1674.198    0.000 1674.198    0.000 layer.py:154(elements)
               99519332   96.603    0.000 1616.681    0.000 activation.py:713(forward)
               11887951   83.246    0.000 1606.625    0.000 agent.py:59(modify_board)
                5313421 1369.915    0.000 1579.186    0.000 agent.py:187(convert_values)
               99519332   86.189    0.000 1520.078    0.000 functional.py:1364(leaky_relu)
               99519332 1417.250    0.000 1417.250    0.000 {built-in method torch._C._nn.leaky_relu}
              129996812 1387.153    0.000 1387.153    0.000 {built-in method clone}
             4684091131  886.951    0.000 1279.401    0.000 enum.py:646(__hash__)
                2193846  972.023    0.000 1273.142    0.001 replaybuffer.py:73(CF_save_data)
                4086165   25.549    0.000 1216.849    0.000 level.py:8(__init__)
                2193846   54.949    0.000 1108.328    0.001 agent.py:172(__call__)
               11887951 1050.445    0.000 1050.445    0.000 {built-in method torch._C._nn.one_hot}
              221879972  235.811    0.000 1049.203    0.000 {built-in method builtins.any}
                2193846   53.142    0.000  987.487    0.000 agent.py:112(__call__)
                4086165  149.035    0.000  950.555    0.000 levels.py:199(generate)
              219327876  683.127    0.000  896.767    0.000 layers.py:77(check)
              122855376  876.303    0.000  876.303    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              219327876  539.167    0.000  846.742    0.000 layers.py:286(check)
             2368282785  671.559    0.000  813.392    0.000 layers.py:809(<genexpr>)
                2193846   63.424    0.000  780.481    0.000 replaybuffer.py:18(stacker)
                6581538  146.476    0.000  774.598    0.000 optimizer.py:189(zero_grad)
              122855376  760.179    0.000  760.179    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              219327876  442.178    0.000  739.904    0.000 layers.py:246(check)
                2193846   62.526    0.000  735.527    0.000 replaybuffer.py:63(stacker)
            10489342164  660.913    0.000  724.667    0.000 {built-in method builtins.len}
              219384600   66.524    0.000  692.271    0.000 {built-in method builtins.all}
                9694105  248.899    0.000  671.889    0.000 exploration.py:53(softmaxer)
                8172330   74.850    0.000  658.328    0.000 level.py:41(notUsed)
              682637137  189.355    0.000  653.569    0.000 layers.py:799(<genexpr>)
              219327876  407.556    0.000  538.550    0.000 layers.py:62(check)
             5682050616  537.885    0.000  537.885    0.000 layer.py:99(positions)
               61427688  516.996    0.000  516.996    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               61427688  450.991    0.000  450.991    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              219384600  306.592    0.000  443.160    0.000 layers.py:113(isDone)
               12560022  170.664    0.000  427.971    0.000 random.py:315(sample)
               87753820  419.812    0.000  419.812    0.000 layer.py:171(<listcomp>)
               61427688  413.716    0.000  413.716    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               61427688  411.391    0.000  411.391    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              219327876  266.139    0.000  409.405    0.000 layers.py:313(check)
               40861650   58.189    0.000  396.371    0.000 layer.py:77(restart)
             4684116362  392.455    0.000  392.455    0.000 {built-in method builtins.hash}
              429993816  298.957    0.000  369.302    0.000 tensor.py:906(grad)
              219327876  227.847    0.000  361.412    0.000 layers.py:273(check)
              246888294  274.259    0.000  356.662    0.000 layer.py:134(remove)
                2193846  202.536    0.000  344.239    0.000 collector.py:46(collect)
                6581538   13.254    0.000  342.715    0.000 loss.py:527(forward)
                6581538   38.267    0.000  329.461    0.000 functional.py:2898(mse_loss)
              219327876  220.809    0.000  327.017    0.000 layers.py:48(check)
               24622056  325.264    0.000  325.264    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              144078609  304.776    0.000  304.776    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               61427688  296.992    0.000  296.992    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              473613583  199.975    0.000  280.291    0.000 layer.py:138(add)
                8172330    9.996    0.000  274.733    0.000 level.py:38(elementsIn)
               87753820  273.532    0.000  273.532    0.000 layer.py:172(<listcomp>)
               51953512   47.044    0.000  262.593    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9621660: <Causal4_Conver4_3counterfacts_2_0> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May  7 14:30:14 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May  7 14:49:19 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May  7 14:49:19 2021
Terminated at Sat May  8 14:44:51 2021
Results reported at Sat May  8 14:44:51 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85908.85 sec.
    Max Memory :                                 7515 MB
    Average Memory :                             5403.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8869.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86133 sec.
    Turnaround time :                            87277 sec.

The output (if any) is above this job summary.

