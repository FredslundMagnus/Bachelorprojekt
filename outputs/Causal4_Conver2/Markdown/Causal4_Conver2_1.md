
# Parameters

    Name :                      Causal4_Conver2-1
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
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65496667192 function calls (65206467581 primitive calls) in 86109.51 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.511 86109.511 {built-in method builtins.exec}
                      1    4.140    4.140 86109.511 86109.511 <string>:1(<module>)
                      1  330.595  330.595 86105.371 86105.371 main.py:79(CFagent)
                9286857   35.633    0.000 29136.005    0.003 agent.py:29(learn)
                9286842  726.064    0.000 24334.577    0.003 learner.py:42(Qlearn)
                3095619   14.749    0.000 18995.723    0.006 game.py:41(step)
                3095619   18.096    0.000 18220.652    0.006 layers.py:718(step)
        324699795/34501875 1414.655    0.000 12658.544    0.000 module.py:866(_call_impl)
                3095619  281.156    0.000 12250.663    0.004 layers.py:17(step)
              309505253  903.489    0.000 11943.005    0.000 layer.py:98(move)
               25215033   81.235    0.000 11880.299    0.000 network.py:27(forward)
               25215033  380.928    0.000 11632.056    0.000 container.py:117(forward)
                3095619  314.303    0.000 11237.227    0.004 agent.py:54(_learn)
                3095619  311.655    0.000 10420.503    0.003 agent.py:204(_learn)
                9286842   84.404    0.000 10345.489    0.001 optimizer.py:84(wrapper)
                3095619  956.562    0.000 10074.538    0.003 agent.py:212(counterfact)
                9286842   40.976    0.000 9950.906    0.001 grad_mode.py:24(decorate_context)
                9286842  280.934    0.000 9814.040    0.001 adam.py:55(step)
                9286842 2024.123    0.000 9213.794    0.001 _functional.py:53(adam)
              309505253 1496.296    0.000 7481.930    0.000 layers.py:735(check)
                3095619   93.705    0.000 7421.675    0.002 agent.py:117(_learn)
                7962734  215.316    0.000 6043.194    0.001 agent.py:49(__call__)
                3095619 3150.890    0.001 5993.267    0.002 replaybuffer.py:28(teleporter_save_data)
                9286842   40.760    0.000 5992.806    0.001 tensor.py:195(backward)
                9286842   37.361    0.000 5950.518    0.001 __init__.py:68(backward)
                3095620  452.515    0.000 5928.783    0.002 layers.py:684(update)
                9286842 5696.167    0.001 5696.167    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3095619 3008.077    0.001 5355.561    0.002 agent.py:88(interveen)
               49284565 5233.675    0.000 5233.675    0.000 {built-in method tensor}
               42137200   31.427    0.000 5023.912    0.000 game.py:37(board)
                3095619 3741.603    0.001 4758.632    0.002 replaybuffer.py:22(sample_data)
                3095619 3535.774    0.001 4530.038    0.001 replaybuffer.py:67(sample_data)
               50430066  122.005    0.000 4147.170    0.000 conv.py:398(forward)
               50430066   70.570    0.000 3974.257    0.000 conv.py:390(_conv_forward)
               50430066 3903.687    0.000 3903.687    0.000 {built-in method conv2d}
               61912390 2216.711    0.000 3813.503    0.000 layer.py:151(update)
               69453861  151.814    0.000 3387.457    0.000 linear.py:93(forward)
               69453861   69.555    0.000 3164.741    0.000 functional.py:1737(linear)
               69453861 3079.056    0.000 3079.056    0.000 {built-in method torch._C._nn.linear}
              309505253  611.204    0.000 2958.625    0.000 layers.py:729(isFree)
                1774234   40.409    0.000 2841.127    0.002 agent.py:176(choose_action)
                3095619 1858.318    0.001 2792.697    0.001 agent.py:67(modify)
              190645073 2597.323    0.000 2597.323    0.000 {built-in method clone}
             2966481968 1902.126    0.000 2347.421    0.000 layer.py:95(isFree)
              173354364 1882.737    0.000 1882.737    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94668894   78.782    0.000 1882.249    0.000 activation.py:713(forward)
               94668894   89.085    0.000 1803.467    0.000 functional.py:1364(leaky_relu)
               42014468 1758.944    0.000 1758.944    0.000 {built-in method cat}
               94668894 1697.578    0.000 1697.578    0.000 {built-in method torch._C._nn.leaky_relu}
               11058353   77.103    0.000 1665.024    0.000 agent.py:59(modify_board)
              173354364 1659.200    0.000 1659.200    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3095604   52.595    0.000 1635.027    0.001 agent.py:172(__call__)
             5908531111 1065.679    0.000 1542.548    0.000 enum.py:646(__hash__)
                3095619   50.828    0.000 1531.009    0.000 agent.py:112(__call__)
                9286842  232.721    0.000 1448.988    0.000 optimizer.py:189(zero_grad)
              309442082  320.729    0.000 1406.262    0.000 {built-in method builtins.any}
                3095619 1061.502    0.000 1384.371    0.000 replaybuffer.py:73(CF_save_data)
              309505253  896.264    0.000 1182.081    0.000 layers.py:77(check)
                3215538   38.519    0.000 1166.715    0.000 layers.py:740(restart)
             3369811082  893.716    0.000 1085.533    0.000 layers.py:700(<genexpr>)
              309505253  652.592    0.000 1055.659    0.000 layers.py:246(check)
               11058353 1054.674    0.000 1054.674    0.000 {built-in method torch._C._nn.one_hot}
               86677182 1030.075    0.000 1030.075    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              309505253  608.885    0.000 1004.997    0.000 layers.py:286(check)
               86677182  889.205    0.000  889.205    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1098055899  882.275    0.000  882.275    0.000 layer.py:146(elements)
               86677182  854.402    0.000  854.402    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86677182  845.277    0.000  845.277    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3215538   17.701    0.000  823.851    0.000 level.py:8(__init__)
                3095619   59.237    0.000  790.541    0.000 replaybuffer.py:18(stacker)
                3095604   61.790    0.000  775.235    0.000 replaybuffer.py:63(stacker)
              309562000  113.616    0.000  713.129    0.000 {built-in method builtins.all}
             7829107360  692.808    0.000  692.808    0.000 layer.py:91(positions)
                3095619  403.401    0.000  670.097    0.000 collector.py:46(collect)
                3215538  106.159    0.000  664.090    0.000 levels.py:199(generate)
               86677182  664.016    0.000  664.016    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              204799030  656.964    0.000  656.964    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1080494932  276.732    0.000  636.849    0.000 layers.py:690(<genexpr>)
        8150382745/8150382742  557.445    0.000  622.764    0.000 {built-in method builtins.len}
                7962734  225.991    0.000  616.600    0.000 exploration.py:53(softmaxer)
              309505253  441.571    0.000  590.600    0.000 layers.py:62(check)
              309505253  352.495    0.000  542.030    0.000 layers.py:273(check)
              309505253  346.854    0.000  538.459    0.000 layers.py:313(check)
              606740358  426.286    0.000  534.743    0.000 tensor.py:906(grad)
                1774234  454.703    0.000  519.682    0.000 agent.py:187(convert_values)
               12622314  184.583    0.000  485.349    0.000 random.py:315(sample)
             5908566422  476.876    0.000  476.876    0.000 {built-in method builtins.hash}
                9286842   13.735    0.000  473.966    0.000 loss.py:527(forward)
                9286842   38.025    0.000  460.231    0.000 functional.py:2898(mse_loss)
                6431076   53.998    0.000  452.390    0.000 level.py:41(notUsed)
              309505253  292.865    0.000  434.217    0.000 layers.py:48(check)
              309505253  232.500    0.000  339.273    0.000 layers.py:23(check)
               50430066   35.581    0.000  312.324    0.000 flatten.py:39(forward)
                9286842  302.734    0.000  302.734    0.000 {built-in method torch._C._nn.mse_loss}
               32155380   43.509    0.000  293.717    0.000 layer.py:69(restart)
              305414107  209.300    0.000  291.241    0.000 layer.py:126(remove)
               18573714  282.628    0.000  282.628    0.000 {built-in method sum}
               50430066  276.744    0.000  276.744    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              488265108  202.116    0.000  275.131    0.000 layer.py:130(add)
             3417356663  271.243    0.000  271.243    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579164: <Causal4_Conver2_1> in cluster <dcc> Done

Job <Causal4_Conver2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:43:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:43:18 2021
Terminated at Thu Apr 29 08:38:33 2021
Results reported at Thu Apr 29 08:38:33 2021

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

    CPU time :                                   85896.80 sec.
    Max Memory :                                 8596 MB
    Average Memory :                             5773.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7788.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            194067 sec.

The output (if any) is above this job summary.

