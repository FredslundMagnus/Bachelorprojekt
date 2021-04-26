
# Parameters

    Name :                      Causal4_Cf_convert1_TopN3-0
    Main :                      CFagent
    Level :                     Levels.Causal4
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


      65700258815 function calls (65422000956 primitive calls) in 86118.20 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.202 86118.202 {built-in method builtins.exec}
                      1    5.254    5.254 86118.202 86118.202 <string>:1(<module>)
                      1  401.686  401.686 86112.947 86112.947 main.py:79(CFagent)
                8669214   42.885    0.000 23305.788    0.003 agent.py:29(learn)
                2889738   16.591    0.000 20790.747    0.007 game.py:41(step)
                2889738   19.764    0.000 20048.404    0.007 layers.py:718(step)
                8669211  608.629    0.000 18772.160    0.002 learner.py:42(Qlearn)
                2889738  292.171    0.000 12454.930    0.004 layers.py:17(step)
              288962081  858.205    0.000 12135.076    0.000 layer.py:98(move)
                2889738 1290.117    0.000 11005.035    0.004 agent.py:210(counterfact)
        311076639/32820471 1375.174    0.000 10941.939    0.000 module.py:866(_call_impl)
               24151260   69.314    0.000 10157.078    0.000 network.py:27(forward)
               24151260  353.577    0.000 9908.549    0.000 container.py:117(forward)
                2889738  373.151    0.000 9080.563    0.003 agent.py:54(_learn)
                2889738  366.357    0.000 8170.279    0.003 agent.py:202(_learn)
                2889738 6647.773    0.002 7659.186    0.003 replaybuffer.py:22(sample_data)
                2889739  457.087    0.000 7539.566    0.003 layers.py:684(update)
                2889738 6306.368    0.002 7271.786    0.003 replaybuffer.py:67(sample_data)
              288962081 1362.694    0.000 7263.368    0.000 layers.py:735(check)
                8669211   97.221    0.000 7097.732    0.001 optimizer.py:84(wrapper)
                8669211   49.147    0.000 6695.380    0.001 grad_mode.py:24(decorate_context)
                8669211  313.722    0.000 6535.006    0.001 adam.py:55(step)
                2889738  104.743    0.000 5989.303    0.002 agent.py:117(_learn)
                8669211 1349.898    0.000 5909.277    0.001 _functional.py:53(adam)
                7739782  269.117    0.000 5544.550    0.001 agent.py:49(__call__)
               48335331 5253.290    0.000 5253.290    0.000 {built-in method tensor}
                8669211   43.877    0.000 5090.157    0.001 tensor.py:195(backward)
               41642585   30.173    0.000 5078.988    0.000 game.py:37(board)
                8669211   46.877    0.000 5044.984    0.001 __init__.py:68(backward)
                2889738 2883.777    0.001 4924.905    0.002 replaybuffer.py:28(teleporter_save_data)
               57794770 2905.772    0.000 4895.181    0.000 layer.py:151(update)
                8669211 4797.664    0.001 4797.664    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2889738 2484.997    0.001 4488.608    0.002 agent.py:88(interveen)
               48302520  112.681    0.000 3705.659    0.000 conv.py:398(forward)
               48302520   78.493    0.000 3534.038    0.000 conv.py:390(_conv_forward)
               48302520 3455.545    0.000 3455.545    0.000 {built-in method conv2d}
              288962081  607.631    0.000 3395.893    0.000 layers.py:729(isFree)
             2800305533 2335.058    0.000 2788.262    0.000 layer.py:95(isFree)
               66674304  136.085    0.000 2787.802    0.000 linear.py:93(forward)
                1962794   48.485    0.000 2710.622    0.001 agent.py:175(choose_action)
               66674304   57.595    0.000 2573.209    0.000 functional.py:1737(linear)
               66674304 2501.144    0.000 2501.144    0.000 {built-in method torch._C._nn.linear}
                2889738 1607.060    0.001 2440.672    0.001 agent.py:67(modify)
              200510841 2018.763    0.000 2018.763    0.000 {built-in method clone}
                5002939   61.743    0.000 1879.795    0.000 layers.py:740(restart)
               39526885 1612.476    0.000 1612.476    0.000 {built-in method cat}
               10629520   82.528    0.000 1566.108    0.000 agent.py:59(modify_board)
                2889738 1179.849    0.000 1535.448    0.001 replaybuffer.py:73(CF_save_data)
             5847442518 1063.004    0.000 1508.039    0.000 enum.py:646(__hash__)
               90825564   87.075    0.000 1446.034    0.000 activation.py:713(forward)
                2889735   65.284    0.000 1424.335    0.000 agent.py:171(__call__)
               90825564   78.565    0.000 1358.959    0.000 functional.py:1364(leaky_relu)
                5002939   30.284    0.000 1319.676    0.000 level.py:8(__init__)
                2889738   63.519    0.000 1302.033    0.000 agent.py:112(__call__)
              286860700  302.622    0.000 1292.608    0.000 {built-in method builtins.any}
               90825564 1264.797    0.000 1264.797    0.000 {built-in method torch._C._nn.leaky_relu}
             1293184225 1256.454    0.000 1256.454    0.000 layer.py:146(elements)
              288973900  190.425    0.000 1182.298    0.000 {built-in method builtins.all}
              161825268 1160.578    0.000 1160.578    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              288962081  874.711    0.000 1145.778    0.000 layers.py:77(check)
              288962081  749.261    0.000 1144.916    0.000 layers.py:246(check)
                5002939  175.783    0.000 1062.080    0.000 levels.py:199(generate)
               10629520 1042.411    0.000 1042.411    0.000 {built-in method torch._C._nn.one_hot}
             2139485518  597.807    0.000 1027.839    0.000 layers.py:690(<genexpr>)
              161825268 1004.221    0.000 1004.221    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8669211  182.792    0.000  997.040    0.000 optimizer.py:189(zero_grad)
             3123680571  813.831    0.000  989.986    0.000 layers.py:700(<genexpr>)
              288962081  578.212    0.000  965.345    0.000 layers.py:286(check)
                2889738   65.382    0.000  758.579    0.000 replaybuffer.py:18(stacker)
                2889735   69.569    0.000  724.221    0.000 replaybuffer.py:63(stacker)
               10005878   82.500    0.000  714.683    0.000 level.py:41(notUsed)
              288962081  543.470    0.000  695.136    0.000 layers.py:62(check)
               80912634  670.241    0.000  670.241    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7308945606  669.647    0.000  669.647    0.000 layer.py:91(positions)
                7739782  204.130    0.000  600.104    0.000 exploration.py:53(softmaxer)
               80912634  590.559    0.000  590.559    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               15785354  221.544    0.000  568.628    0.000 random.py:315(sample)
        7449879715/7449879712  503.089    0.000  563.312    0.000 {built-in method builtins.len}
               80912634  556.940    0.000  556.940    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               80912634  552.201    0.000  552.201    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50029390   69.343    0.000  481.798    0.000 layer.py:69(restart)
              288962081  309.207    0.000  481.456    0.000 layers.py:313(check)
                8669211   18.280    0.000  474.570    0.000 loss.py:527(forward)
              566388522  382.148    0.000  473.974    0.000 tensor.py:906(grad)
                8669211   49.445    0.000  456.290    0.000 functional.py:2898(mse_loss)
              288962081  284.816    0.000  453.994    0.000 layers.py:273(check)
                2889738  262.791    0.000  451.447    0.000 collector.py:46(collect)
             5847475477  445.041    0.000  445.041    0.000 {built-in method builtins.hash}
              214030096  421.650    0.000  421.650    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              288962081  280.330    0.000  407.606    0.000 layers.py:48(check)
               80912634  389.366    0.000  389.366    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              304667242  284.055    0.000  384.619    0.000 layer.py:126(remove)
                1962794  384.291    0.000  384.291    0.000 agent.py:186(convert_values)
              591031849  255.624    0.000  356.298    0.000 layer.py:130(add)
              288962081  221.161    0.000  323.709    0.000 layers.py:23(check)
              390920499  193.090    0.000  283.644    0.000 random.py:250(_randbelow_with_getrandbits)
              203367713  283.106    0.000  283.106    0.000 level.py:32(inverse)
               10005878   12.044    0.000  275.465    0.000 level.py:38(elementsIn)
               57794770  273.172    0.000  273.172    0.000 layer.py:163(<listcomp>)
                8669211  271.039    0.000  271.039    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551809: <Causal4_Cf_convert1_TopN3_0> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:30 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 03:28:01 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 03:28:01 2021
Terminated at Thu Apr 22 03:23:29 2021
Results reported at Thu Apr 22 03:23:29 2021

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

    CPU time :                                   85909.17 sec.
    Max Memory :                                 8474 MB
    Average Memory :                             5809.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7910.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            86579 sec.

The output (if any) is above this job summary.

