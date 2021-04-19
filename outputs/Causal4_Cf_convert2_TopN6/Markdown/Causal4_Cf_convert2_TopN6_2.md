
# Parameters

    Name :                      Causal4_Cf_convert2_TopN6-2
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69471478764 function calls (69174619717 primitive calls) in 86118.06 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.058 86118.058 {built-in method builtins.exec}
                      1    4.631    4.631 86118.058 86118.058 <string>:1(<module>)
                      1  393.998  393.998 86113.427 86113.427 main.py:79(CFagent)
                9564489   44.408    0.000 24437.248    0.003 agent.py:29(learn)
                3188163   17.671    0.000 21399.517    0.007 game.py:41(step)
                3188163   23.032    0.000 20620.421    0.006 layers.py:718(step)
                9564486  615.680    0.000 19761.669    0.002 learner.py:42(Qlearn)
                3188163  310.545    0.000 13437.002    0.004 layers.py:17(step)
              318756135  942.557    0.000 13098.179    0.000 layer.py:98(move)
        332222676/35365320 1395.160    0.000 11176.665    0.000 module.py:866(_call_impl)
               25800834   70.560    0.000 10402.350    0.000 network.py:27(forward)
               25800834  334.867    0.000 10156.685    0.000 container.py:117(forward)
                3188163  855.216    0.000 10097.835    0.003 agent.py:210(counterfact)
                3188163  391.028    0.000 9523.431    0.003 agent.py:54(_learn)
                3188163  380.374    0.000 8630.023    0.003 agent.py:202(_learn)
              318756135 1480.546    0.000 7909.788    0.000 layers.py:735(check)
                3188163 6742.215    0.002 7790.858    0.002 replaybuffer.py:22(sample_data)
                9564486   95.096    0.000 7638.349    0.001 optimizer.py:84(wrapper)
                9564486   50.149    0.000 7243.243    0.001 grad_mode.py:24(decorate_context)
                3188163 6230.682    0.002 7223.763    0.002 replaybuffer.py:67(sample_data)
                3188164  488.597    0.000 7126.226    0.002 layers.py:684(update)
                9564486  312.465    0.000 7083.993    0.001 adam.py:55(step)
                9564486 1462.329    0.000 6432.534    0.001 _functional.py:53(adam)
                3188163  104.476    0.000 6216.597    0.002 agent.py:117(_learn)
                8116236  242.099    0.000 5486.150    0.001 agent.py:49(__call__)
               50449831 5325.666    0.000 5325.666    0.000 {built-in method tensor}
                9564486   40.214    0.000 5238.660    0.001 tensor.py:195(backward)
                9564486   43.377    0.000 5197.075    0.001 __init__.py:68(backward)
               43098895   28.221    0.000 5136.965    0.000 game.py:37(board)
                9564486 4952.697    0.001 4952.697    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               63763270 2734.826    0.000 4702.445    0.000 layer.py:151(update)
                3188163 2519.193    0.001 4335.817    0.001 replaybuffer.py:28(teleporter_save_data)
                3188163 2191.859    0.001 4307.329    0.001 agent.py:88(interveen)
               51601668  115.237    0.000 3788.870    0.000 conv.py:398(forward)
               51601668   74.645    0.000 3614.902    0.000 conv.py:390(_conv_forward)
              318756135  629.379    0.000 3579.302    0.000 layers.py:729(isFree)
               51601668 3540.257    0.000 3540.257    0.000 {built-in method conv2d}
             3080858760 2450.092    0.000 2949.924    0.000 layer.py:95(isFree)
               71026176  145.676    0.000 2850.667    0.000 linear.py:93(forward)
               71026176   57.527    0.000 2626.564    0.000 functional.py:1737(linear)
               71026176 2554.761    0.000 2554.761    0.000 {built-in method torch._C._nn.linear}
                3188163 1650.864    0.001 2508.719    0.001 agent.py:67(modify)
                1743789   39.877    0.000 2420.236    0.001 agent.py:175(choose_action)
              170561296 1741.118    0.000 1741.118    0.000 {built-in method clone}
             6252381841 1170.780    0.000 1684.505    0.000 enum.py:646(__hash__)
               43186014 1662.029    0.000 1662.029    0.000 {built-in method cat}
               11304399   74.680    0.000 1565.802    0.000 agent.py:59(modify_board)
               96827010   82.212    0.000 1498.059    0.000 activation.py:713(forward)
                3188160   62.529    0.000 1485.078    0.000 agent.py:171(__call__)
              318907412  335.500    0.000 1477.120    0.000 {built-in method builtins.any}
               96827010   81.135    0.000 1415.847    0.000 functional.py:1364(leaky_relu)
                3188163   60.021    0.000 1387.587    0.000 agent.py:112(__call__)
              318816400  174.101    0.000 1345.485    0.000 {built-in method builtins.all}
               96827010 1318.894    0.000 1318.894    0.000 {built-in method torch._C._nn.leaky_relu}
              318756135  966.792    0.000 1270.902    0.000 layers.py:77(check)
              178537068 1260.798    0.000 1260.798    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1958813762  521.233    0.000 1211.345    0.000 layers.py:690(<genexpr>)
              318756135  777.625    0.000 1206.024    0.000 layers.py:246(check)
                3097152   41.797    0.000 1189.980    0.000 layers.py:740(restart)
             1100629545 1181.163    0.000 1181.163    0.000 layer.py:146(elements)
                3188163  928.228    0.000 1167.283    0.000 replaybuffer.py:73(CF_save_data)
             3472911728  939.116    0.000 1141.620    0.000 layers.py:700(<genexpr>)
              178537068 1110.372    0.000 1110.372    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9564486  197.932    0.000 1097.346    0.000 optimizer.py:189(zero_grad)
              318756135  638.165    0.000 1065.298    0.000 layers.py:286(check)
               11304399 1040.569    0.000 1040.569    0.000 {built-in method torch._C._nn.one_hot}
                3097152   20.130    0.000  838.328    0.000 level.py:8(__init__)
             8367476751  788.913    0.000  788.913    0.000 layer.py:91(positions)
                3188163   71.234    0.000  786.967    0.000 replaybuffer.py:18(stacker)
                3188160   67.183    0.000  743.761    0.000 replaybuffer.py:63(stacker)
               89268534  731.723    0.000  731.723    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              318756135  550.030    0.000  709.692    0.000 layers.py:62(check)
                3097152  108.971    0.000  663.848    0.000 levels.py:199(generate)
               89268534  644.835    0.000  644.835    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8297390516/8297390513  552.144    0.000  612.907    0.000 {built-in method builtins.len}
               89268534  599.862    0.000  599.862    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89268534  597.918    0.000  597.918    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              318816400  403.663    0.000  595.108    0.000 layers.py:113(isDone)
                8116236  201.831    0.000  571.312    0.000 exploration.py:53(softmaxer)
               12570630  212.755    0.000  552.014    0.000 random.py:315(sample)
              318756135  339.314    0.000  537.025    0.000 layers.py:313(check)
              318756135  330.437    0.000  529.161    0.000 layers.py:273(check)
              624879822  422.083    0.000  522.202    0.000 tensor.py:906(grad)
             6252418160  513.731    0.000  513.731    0.000 {built-in method builtins.hash}
                3188163  289.787    0.000  494.949    0.000 collector.py:46(collect)
                9564486   19.420    0.000  465.263    0.000 loss.py:527(forward)
              318756135  306.917    0.000  450.365    0.000 layers.py:48(check)
                6194304   54.052    0.000  449.256    0.000 level.py:41(notUsed)
                1743789  393.253    0.000  446.125    0.000 agent.py:186(convert_values)
                9564486   44.465    0.000  445.843    0.000 functional.py:2898(mse_loss)
               89268534  434.636    0.000  434.636    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              185053855  374.075    0.000  374.075    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              318756135  231.150    0.000  345.825    0.000 layers.py:23(check)
              310040989  213.148    0.000  305.139    0.000 layer.py:126(remove)
               30971520   44.253    0.000  299.325    0.000 layer.py:69(restart)
              487603830  211.517    0.000  291.214    0.000 layer.py:130(add)
             3518857269  287.734    0.000  287.734    0.000 {method 'random' of '_random.Random' objects}
               63763270  275.572    0.000  275.572    0.000 layer.py:163(<listcomp>)
              400218329  184.404    0.000  272.617    0.000 random.py:250(_randbelow_with_getrandbits)
                9564486  272.043    0.000  272.043    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533960: <Causal4_Cf_convert2_TopN6_2> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN6_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:09 2021
Terminated at Mon Apr 19 20:15:41 2021
Results reported at Mon Apr 19 20:15:41 2021

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

    CPU time :                                   85808.17 sec.
    Max Memory :                                 8821 MB
    Average Memory :                             5798.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7563.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86239 sec.
    Turnaround time :                            86134 sec.

The output (if any) is above this job summary.

