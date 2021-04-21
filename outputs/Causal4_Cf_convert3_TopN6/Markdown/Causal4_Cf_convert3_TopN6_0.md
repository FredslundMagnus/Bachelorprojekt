
# Parameters

    Name :                      Causal4_Cf_convert3_TopN6-0
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69786987575 function calls (69478325220 primitive calls) in 86118.03 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.033 86118.033 {built-in method builtins.exec}
                      1    4.525    4.525 86118.033 86118.033 <string>:1(<module>)
                      1  410.175  410.175 86113.508 86113.508 main.py:79(CFagent)
               10064376   41.188    0.000 25735.567    0.003 agent.py:29(learn)
                3354792   15.445    0.000 21817.248    0.007 game.py:41(step)
                3354792   20.737    0.000 20974.601    0.006 layers.py:718(step)
               10064376  654.402    0.000 20824.198    0.002 learner.py:42(Qlearn)
                3354792  328.257    0.000 14232.399    0.004 layers.py:17(step)
              335124808 1014.958    0.000 13874.872    0.000 layer.py:98(move)
        345565026/36904362 1479.838    0.000 11746.808    0.000 module.py:866(_call_impl)
               26839986   77.261    0.000 10953.165    0.000 network.py:27(forward)
               26839986  365.253    0.000 10688.002    0.000 container.py:117(forward)
                3354792  889.927    0.000 10487.267    0.003 agent.py:210(counterfact)
                3354792  405.260    0.000 10021.949    0.003 agent.py:54(_learn)
                3354792  395.702    0.000 9132.388    0.003 agent.py:202(_learn)
              335124808 1602.697    0.000 8496.068    0.000 layers.py:735(check)
               10064376   94.928    0.000 8108.038    0.001 optimizer.py:84(wrapper)
               10064376   49.083    0.000 7704.136    0.001 grad_mode.py:24(decorate_context)
               10064376  330.156    0.000 7542.999    0.001 adam.py:55(step)
                3354792 6095.775    0.002 7220.059    0.002 replaybuffer.py:22(sample_data)
                3354792 5794.187    0.002 6858.605    0.002 replaybuffer.py:67(sample_data)
               10064376 1555.214    0.000 6847.581    0.001 _functional.py:53(adam)
                3354793  508.378    0.000 6688.688    0.002 layers.py:684(update)
                3354792  109.182    0.000 6516.148    0.002 agent.py:117(_learn)
               52756279 5869.180    0.000 5869.180    0.000 {built-in method tensor}
                8380568  238.114    0.000 5678.276    0.001 agent.py:49(__call__)
               45037550   28.813    0.000 5665.217    0.000 game.py:37(board)
               10064376   42.476    0.000 5409.062    0.001 tensor.py:195(backward)
               10064376   46.782    0.000 5365.121    0.001 __init__.py:68(backward)
               10064376 5105.890    0.001 5105.890    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               67095850 2748.190    0.000 4716.861    0.000 layer.py:151(update)
               53679972  127.832    0.000 3977.007    0.000 conv.py:398(forward)
                3354792 1703.092    0.001 3938.276    0.001 agent.py:88(interveen)
               53679972   80.597    0.000 3786.490    0.000 conv.py:390(_conv_forward)
               53679972 3705.893    0.000 3705.893    0.000 {built-in method conv2d}
              335124808  654.187    0.000 3666.990    0.000 layers.py:729(isFree)
                3354792 1901.974    0.001 3227.907    0.001 replaybuffer.py:28(teleporter_save_data)
             3008702311 2488.806    0.000 3012.802    0.000 layer.py:95(isFree)
               73810374  158.534    0.000 2987.192    0.000 linear.py:93(forward)
               73810374   63.454    0.000 2745.153    0.000 functional.py:1737(linear)
               73810374 2666.237    0.000 2666.237    0.000 {built-in method torch._C._nn.linear}
                3354792 1713.094    0.001 2612.551    0.001 agent.py:67(modify)
                1685458   37.977    0.000 2298.443    0.001 agent.py:175(choose_action)
               45283280 1800.300    0.000 1800.300    0.000 {built-in method cat}
             6244751889 1187.172    0.000 1675.004    0.000 enum.py:646(__hash__)
               11735360   82.916    0.000 1625.998    0.000 agent.py:59(modify_board)
              100650360   86.978    0.000 1586.303    0.000 activation.py:713(forward)
                3354792   63.958    0.000 1580.638    0.000 agent.py:171(__call__)
              335739505  348.577    0.000 1550.758    0.000 {built-in method builtins.any}
              100650360   86.935    0.000 1499.325    0.000 functional.py:1364(leaky_relu)
                3354792   60.736    0.000 1462.947    0.000 agent.py:112(__call__)
              100650360 1396.574    0.000 1396.574    0.000 {built-in method torch._C._nn.leaky_relu}
              335124808 1038.333    0.000 1375.781    0.000 layers.py:77(check)
              187868352 1346.616    0.000 1346.616    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              128837179 1331.884    0.000 1331.884    0.000 {built-in method clone}
                3094588   42.100    0.000 1203.325    0.000 layers.py:740(restart)
             3656231832  992.588    0.000 1202.181    0.000 layers.py:700(<genexpr>)
                3354792  960.149    0.000 1198.865    0.000 replaybuffer.py:73(CF_save_data)
              187868352 1183.225    0.000 1183.225    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10064376  212.916    0.000 1181.872    0.000 optimizer.py:189(zero_grad)
              335124808  757.236    0.000 1165.559    0.000 layers.py:286(check)
             1084934495 1139.006    0.000 1139.006    0.000 layer.py:146(elements)
              335124808  712.307    0.000 1138.004    0.000 layers.py:246(check)
               11735360 1079.081    0.000 1079.081    0.000 {built-in method torch._C._nn.one_hot}
                3354792   70.290    0.000  855.535    0.000 replaybuffer.py:18(stacker)
                3094588   19.624    0.000  847.451    0.000 level.py:8(__init__)
                3354792   67.764    0.000  807.921    0.000 replaybuffer.py:63(stacker)
              335479300  141.005    0.000  801.334    0.000 {built-in method builtins.all}
             8100508284  773.483    0.000  773.483    0.000 layer.py:91(positions)
               93934176  772.511    0.000  772.511    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              335124808  605.467    0.000  767.857    0.000 layers.py:62(check)
             1547188447  420.650    0.000  700.701    0.000 layers.py:690(<genexpr>)
               93934176  680.535    0.000  680.535    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3094588  110.948    0.000  673.656    0.000 levels.py:199(generate)
        8891540331/8891540328  592.078    0.000  658.663    0.000 {built-in method builtins.len}
               93934176  644.197    0.000  644.197    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               93934176  639.794    0.000  639.794    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              335124808  419.022    0.000  634.429    0.000 layers.py:273(check)
              335124808  390.730    0.000  593.866    0.000 layers.py:313(check)
                8380568  207.723    0.000  578.290    0.000 exploration.py:53(softmaxer)
              657539316  453.759    0.000  568.199    0.000 tensor.py:906(grad)
               12898760  220.382    0.000  565.378    0.000 random.py:315(sample)
                3354792  311.588    0.000  527.923    0.000 collector.py:46(collect)
              335124808  346.327    0.000  500.648    0.000 layers.py:48(check)
             6244790112  487.839    0.000  487.839    0.000 {built-in method builtins.hash}
               10064376   17.268    0.000  472.932    0.000 loss.py:527(forward)
               93934176  461.287    0.000  461.287    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10064376   44.245    0.000  455.664    0.000 functional.py:2898(mse_loss)
                6189176   54.874    0.000  455.460    0.000 level.py:41(notUsed)
              335124808  264.074    0.000  382.441    0.000 layers.py:23(check)
                1685458  356.303    0.000  377.589    0.000 agent.py:186(convert_values)
              290805596  235.396    0.000  319.810    0.000 layer.py:126(remove)
             3699365836  303.439    0.000  303.439    0.000 {method 'random' of '_random.Random' objects}
               30945880   47.173    0.000  302.791    0.000 layer.py:69(restart)
              143927331  302.526    0.000  302.526    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              476031302  210.097    0.000  285.967    0.000 layer.py:130(add)
                6709586  281.488    0.000  281.488    0.000 {built-in method nonzero}
             2345131248  281.300    0.000  281.300    0.000 layer.py:203(isBlocking)
               67095850  278.091    0.000  278.091    0.000 layer.py:163(<listcomp>)
               10064376  276.001    0.000  276.001    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533961: <Causal4_Cf_convert3_TopN6_0> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 20:15:43 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 20:15:43 2021
Terminated at Tue Apr 20 20:11:11 2021
Results reported at Tue Apr 20 20:11:11 2021

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

    CPU time :                                   85891.69 sec.
    Max Memory :                                 9475 MB
    Average Memory :                             6268.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6909.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86130 sec.
    Turnaround time :                            172264 sec.

The output (if any) is above this job summary.

