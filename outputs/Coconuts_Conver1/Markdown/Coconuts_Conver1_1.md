
# Parameters

    Name :                      Coconuts_Conver1-1
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
    Hours :                     24.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60440887566 function calls (60151518731 primitive calls) in 86121.96 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.960 86121.960 {built-in method builtins.exec}
                      1    4.347    4.347 86121.960 86121.960 <string>:1(<module>)
                      1  361.966  361.966 86117.613 86117.613 main.py:79(CFagent)
                9782571   40.112    0.000 32033.322    0.003 agent.py:29(learn)
                9782571  784.794    0.000 26746.090    0.003 learner.py:42(Qlearn)
                3260857   16.341    0.000 19310.229    0.006 game.py:41(step)
                3260857   19.130    0.000 18564.812    0.006 layers.py:718(step)
        324350596/34983452 1494.509    0.000 13100.249    0.000 module.py:866(_call_impl)
                3260857  300.296    0.000 12443.259    0.004 layers.py:17(step)
                3260857  355.503    0.000 12350.755    0.004 agent.py:54(_learn)
               25200881   76.618    0.000 12258.182    0.000 network.py:27(forward)
              325901777 1243.021    0.000 12113.016    0.000 layer.py:98(move)
               25200881  381.275    0.000 12001.285    0.000 container.py:117(forward)
                3260857  352.398    0.000 11458.751    0.004 agent.py:204(_learn)
                9782571   89.946    0.000 11328.239    0.001 optimizer.py:84(wrapper)
                9782571   44.338    0.000 10900.045    0.001 grad_mode.py:24(decorate_context)
                9782571  308.595    0.000 10759.242    0.001 adam.py:55(step)
                9782571 2204.160    0.000 10103.538    0.001 _functional.py:53(adam)
                3260857  104.957    0.000 8159.509    0.003 agent.py:117(_learn)
              325901777 1219.934    0.000 7415.736    0.000 layers.py:735(check)
                9782571   43.131    0.000 6715.108    0.001 tensor.py:195(backward)
                9782571   39.523    0.000 6670.290    0.001 __init__.py:68(backward)
                3260857  524.836    0.000 6411.199    0.002 agent.py:212(counterfact)
                9782571 6395.342    0.001 6395.342    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3260858  506.865    0.000 6075.541    0.002 layers.py:684(update)
                7704985  213.019    0.000 6059.952    0.001 agent.py:49(__call__)
                3260857 4475.856    0.001 5604.279    0.002 replaybuffer.py:22(sample_data)
                3260857 4254.780    0.001 5346.552    0.002 replaybuffer.py:67(sample_data)
                3260857 2541.073    0.001 5088.701    0.002 agent.py:88(interveen)
                3260857 2645.430    0.001 4976.495    0.002 replaybuffer.py:28(teleporter_save_data)
               50401762  120.929    0.000 4278.629    0.000 conv.py:398(forward)
               50401762   77.979    0.000 4102.665    0.000 conv.py:390(_conv_forward)
               50401762 4024.687    0.000 4024.687    0.000 {built-in method conv2d}
               69080929  153.247    0.000 3486.285    0.000 linear.py:93(forward)
               39731783 3310.748    0.000 3310.748    0.000 {built-in method tensor}
               69080929   61.805    0.000 3255.308    0.000 functional.py:1737(linear)
               69080929 3177.342    0.000 3177.342    0.000 {built-in method torch._C._nn.linear}
               45652005 1840.570    0.000 3122.765    0.000 layer.py:151(update)
               32219712   24.526    0.000 3073.684    0.000 game.py:37(board)
                3260857 1975.183    0.001 3000.009    0.001 agent.py:67(modify)
              325901777  497.202    0.000 2577.664    0.000 layers.py:729(isFree)
              325901777 1552.776    0.000 2214.113    0.000 layers.py:471(check)
             2057328065 1736.380    0.000 2080.462    0.000 layer.py:95(isFree)
              145539224 2077.683    0.000 2077.683    0.000 {built-in method clone}
              182607992 2077.345    0.000 2077.345    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              325901777 1442.938    0.000 1978.816    0.000 layers.py:77(check)
               94281810   81.130    0.000 1941.967    0.000 activation.py:713(forward)
               43574412 1917.680    0.000 1917.680    0.000 {built-in method cat}
                1191611   27.911    0.000 1883.916    0.002 agent.py:176(choose_action)
               94281810   88.930    0.000 1860.837    0.000 functional.py:1364(leaky_relu)
              182607992 1821.696    0.000 1821.696    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3260857   59.591    0.000 1794.200    0.001 agent.py:172(__call__)
               94281810 1754.035    0.000 1754.035    0.000 {built-in method torch._C._nn.leaky_relu}
               10965842   85.966    0.000 1712.912    0.000 agent.py:59(modify_board)
                3260857   55.982    0.000 1675.423    0.001 agent.py:112(__call__)
                9782571  254.612    0.000 1571.351    0.000 optimizer.py:189(zero_grad)
             5494820701 1049.988    0.000 1510.474    0.000 enum.py:646(__hash__)
                1680388   20.883    0.000 1267.062    0.001 layers.py:740(restart)
              326085800  155.959    0.000 1259.962    0.000 {built-in method builtins.all}
              327666270  278.380    0.000 1171.653    0.000 {built-in method builtins.any}
             1640250631  463.926    0.000 1148.185    0.000 layers.py:690(<genexpr>)
               91303996 1131.564    0.000 1131.564    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10965842 1079.970    0.000 1079.970    0.000 {built-in method torch._C._nn.one_hot}
                1680388   10.560    0.000 1065.600    0.001 level.py:8(__init__)
                3260857  862.599    0.000 1058.749    0.000 replaybuffer.py:73(CF_save_data)
               91303996  976.256    0.000  976.256    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1680388   75.536    0.000  970.997    0.001 levels.py:262(generate)
               91303996  937.840    0.000  937.840    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91303996  924.721    0.000  924.721    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              325901777  661.728    0.000  893.415    0.000 layers.py:62(check)
             2595243296  727.168    0.000  893.273    0.000 layers.py:700(<genexpr>)
                3260857   64.824    0.000  880.374    0.000 replaybuffer.py:18(stacker)
                3260857   66.778    0.000  852.198    0.000 replaybuffer.py:63(stacker)
               14988823  147.119    0.000  833.885    0.000 level.py:41(notUsed)
             7586619111  764.727    0.000  764.727    0.000 layer.py:91(positions)
                3260857  445.336    0.000  734.195    0.000 collector.py:46(collect)
              951686974  720.821    0.000  720.821    0.000 layer.py:146(elements)
               91303996  716.790    0.000  716.790    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7704985  231.281    0.000  627.319    0.000 exploration.py:53(softmaxer)
              326085800  407.805    0.000  611.911    0.000 layers.py:113(isDone)
              639128056  471.817    0.000  583.915    0.000 tensor.py:906(grad)
              159765923  559.171    0.000  559.171    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        6491442122/6491442119  489.330    0.000  556.322    0.000 {built-in method builtins.len}
                9782571   18.364    0.000  517.552    0.000 loss.py:527(forward)
                9782571   38.858    0.000  499.188    0.000 functional.py:2898(mse_loss)
              325901777  319.634    0.000  478.897    0.000 layers.py:48(check)
                6521714  180.558    0.000  474.714    0.000 random.py:315(sample)
             5494857916  460.494    0.000  460.494    0.000 {built-in method builtins.hash}
               14988823   13.012    0.000  373.539    0.000 level.py:38(elementsIn)
              325901777  256.561    0.000  372.052    0.000 layers.py:23(check)
              336236354  235.666    0.000  346.872    0.000 layer.py:126(remove)
                9782571  331.945    0.000  331.945    0.000 {built-in method torch._C._nn.mse_loss}
               50401762   38.982    0.000  322.300    0.000 flatten.py:39(forward)
               19565142  308.379    0.000  308.379    0.000 {built-in method sum}
                6521716  296.406    0.000  296.406    0.000 {built-in method nonzero}
                9783667  294.356    0.000  294.356    0.000 {built-in method max}
               50401762  283.318    0.000  283.318    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1191611  274.788    0.000  274.788    0.000 agent.py:187(convert_values)
              430656220  194.044    0.000  260.116    0.000 layer.py:130(add)
              332065461  250.269    0.000  250.269    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579167: <Coconuts_Conver1_1> in cluster <dcc> Done

Job <Coconuts_Conver1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:27:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:27:05 2021
Terminated at Fri Apr 30 10:22:50 2021
Results reported at Fri Apr 30 10:22:50 2021

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

    CPU time :                                   85903.10 sec.
    Max Memory :                                 9675 MB
    Average Memory :                             6567.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86145 sec.
    Turnaround time :                            286723 sec.

The output (if any) is above this job summary.

