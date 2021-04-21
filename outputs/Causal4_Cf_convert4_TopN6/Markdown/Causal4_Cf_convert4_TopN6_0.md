
# Parameters

    Name :                      Causal4_Cf_convert4_TopN6-0
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67924695109 function calls (67620594118 primitive calls) in 86109.97 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.968 86109.968 {built-in method builtins.exec}
                      1    3.927    3.927 86109.968 86109.968 <string>:1(<module>)
                      1  323.840  323.840 86106.041 86106.041 main.py:79(CFagent)
                9972924   36.616    0.000 31065.361    0.003 agent.py:29(learn)
                9972910  771.511    0.000 26085.600    0.003 learner.py:42(Qlearn)
                3324308   14.325    0.000 19748.801    0.006 game.py:41(step)
                3324308   21.148    0.000 18928.475    0.006 layers.py:718(step)
        340521921/36422621 1461.948    0.000 12909.589    0.000 module.py:866(_call_impl)
                3324308  297.682    0.000 12820.692    0.004 layers.py:17(step)
              331884888  955.381    0.000 12493.104    0.000 layer.py:98(move)
               26449711   77.686    0.000 12085.914    0.000 network.py:27(forward)
                3324308  312.245    0.000 11951.553    0.004 agent.py:54(_learn)
               26449711  375.270    0.000 11840.679    0.000 container.py:117(forward)
                9972910   87.471    0.000 11183.234    0.001 optimizer.py:84(wrapper)
                3324308  308.265    0.000 11086.869    0.003 agent.py:202(_learn)
                9972910   42.689    0.000 10755.757    0.001 grad_mode.py:24(decorate_context)
                9972910  302.390    0.000 10614.937    0.001 adam.py:55(step)
                9972910 2168.541    0.000 9968.435    0.001 _functional.py:53(adam)
                3324308  880.675    0.000 9968.144    0.003 agent.py:210(counterfact)
                3324308   93.350    0.000 7968.077    0.002 agent.py:117(_learn)
              331884888 1535.342    0.000 7923.815    0.000 layers.py:735(check)
                9972910   50.840    0.000 6508.867    0.001 tensor.py:195(backward)
                9972910   40.001    0.000 6456.519    0.001 __init__.py:68(backward)
                9972910 6182.557    0.001 6182.557    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8230543  191.160    0.000 6091.755    0.001 agent.py:49(__call__)
                3324309  482.154    0.000 6061.387    0.002 layers.py:684(update)
               52010610 5492.362    0.000 5492.362    0.000 {built-in method tensor}
               44359092   29.832    0.000 5266.798    0.000 game.py:37(board)
                3324308 3892.701    0.001 4946.369    0.001 replaybuffer.py:22(sample_data)
                3324308 3687.131    0.001 4725.764    0.001 replaybuffer.py:67(sample_data)
                3324308 1953.892    0.001 4403.969    0.001 agent.py:88(interveen)
               52899422  122.525    0.000 4244.486    0.000 conv.py:398(forward)
               52899422   70.123    0.000 4054.553    0.000 conv.py:390(_conv_forward)
               52899422 3984.430    0.000 3984.430    0.000 {built-in method conv2d}
               66486170 2251.858    0.000 3963.794    0.000 layer.py:151(update)
                3324308 1964.787    0.001 3752.838    0.001 replaybuffer.py:28(teleporter_save_data)
               72700517  160.950    0.000 3441.464    0.000 linear.py:93(forward)
               72700517   62.972    0.000 3204.788    0.000 functional.py:1737(linear)
               72700517 3125.715    0.000 3125.715    0.000 {built-in method torch._C._nn.linear}
              331884888  614.063    0.000 2982.691    0.000 layers.py:729(isFree)
                3324308 1948.841    0.001 2953.889    0.001 agent.py:67(modify)
                1597656   38.441    0.000 2555.501    0.002 agent.py:175(choose_action)
             2796947840 1932.192    0.000 2368.628    0.000 layer.py:95(isFree)
              186160968 2029.475    0.000 2029.475    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               99150228   80.978    0.000 1894.407    0.000 activation.py:713(forward)
               44797861 1814.965    0.000 1814.965    0.000 {built-in method cat}
               99150228   84.660    0.000 1813.429    0.000 functional.py:1364(leaky_relu)
              186160968 1793.830    0.000 1793.830    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11554851   87.434    0.000 1731.265    0.000 agent.py:59(modify_board)
              125770361 1730.719    0.000 1730.719    0.000 {built-in method clone}
               99150228 1710.681    0.000 1710.681    0.000 {built-in method torch._C._nn.leaky_relu}
                3324294   50.142    0.000 1709.226    0.001 agent.py:171(__call__)
             6451828585 1189.251    0.000 1687.618    0.000 enum.py:646(__hash__)
                3324308   48.883    0.000 1594.213    0.000 agent.py:112(__call__)
                9972910  245.469    0.000 1545.479    0.000 optimizer.py:189(zero_grad)
              332885468  335.022    0.000 1464.729    0.000 {built-in method builtins.any}
                3324308 1027.261    0.000 1318.708    0.000 replaybuffer.py:73(CF_save_data)
              331884888  989.833    0.000 1309.771    0.000 layers.py:77(check)
               93080484 1161.831    0.000 1161.831    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3625172749  931.361    0.000 1129.708    0.000 layers.py:700(<genexpr>)
              331884888  727.378    0.000 1116.094    0.000 layers.py:246(check)
               11554851 1091.660    0.000 1091.660    0.000 {built-in method torch._C._nn.one_hot}
                2869741   33.793    0.000 1044.844    0.000 layers.py:740(restart)
              331884888  647.401    0.000 1044.767    0.000 layers.py:286(check)
               93080484  946.664    0.000  946.664    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1048533558  937.301    0.000  937.301    0.000 layer.py:146(elements)
               93080484  923.881    0.000  923.881    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               93080484  914.700    0.000  914.700    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3324308   63.283    0.000  815.165    0.000 replaybuffer.py:18(stacker)
                3324294   64.237    0.000  804.302    0.000 replaybuffer.py:63(stacker)
              332430900   77.154    0.000  787.124    0.000 {built-in method builtins.all}
             8517519481  767.730    0.000  767.730    0.000 layer.py:91(positions)
              682661988  148.527    0.000  751.667    0.000 layers.py:690(<genexpr>)
                2869741   15.870    0.000  743.581    0.000 level.py:8(__init__)
                3324308  430.728    0.000  713.891    0.000 collector.py:46(collect)
               93080484  711.832    0.000  711.832    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        8824661919/8824661916  588.464    0.000  656.992    0.000 {built-in method builtins.len}
              331884888  485.614    0.000  634.537    0.000 layers.py:62(check)
                8230543  233.132    0.000  632.407    0.000 exploration.py:53(softmaxer)
              332430900  405.285    0.000  599.686    0.000 layers.py:113(isDone)
                2869741   95.936    0.000  590.954    0.000 levels.py:199(generate)
              331884888  376.114    0.000  579.110    0.000 layers.py:273(check)
              651563472  464.161    0.000  573.311    0.000 tensor.py:906(grad)
              331884888  341.425    0.000  535.450    0.000 layers.py:313(check)
                1597656  433.825    0.000  514.385    0.000 agent.py:186(convert_values)
               12388098  192.244    0.000  506.100    0.000 random.py:315(sample)
                9972910   15.151    0.000  503.714    0.000 loss.py:527(forward)
             6451866472  498.373    0.000  498.373    0.000 {built-in method builtins.hash}
                9972910   37.630    0.000  488.563    0.000 functional.py:2898(mse_loss)
              331884888  326.949    0.000  479.089    0.000 layers.py:48(check)
              140649506  457.126    0.000  457.126    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5739482   47.089    0.000  401.368    0.000 level.py:41(notUsed)
              331884888  256.911    0.000  373.674    0.000 layers.py:23(check)
                9972910  321.917    0.000  321.917    0.000 {built-in method torch._C._nn.mse_loss}
               52899422   38.166    0.000  319.941    0.000 flatten.py:39(forward)
               19945848  301.602    0.000  301.602    0.000 {built-in method sum}
             3663213211  288.849    0.000  288.849    0.000 {method 'random' of '_random.Random' objects}
                6648618  288.049    0.000  288.049    0.000 {built-in method nonzero}
                9974065  283.103    0.000  283.103    0.000 {built-in method max}
               52899422  281.775    0.000  281.775    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533964: <Causal4_Cf_convert4_TopN6_0> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 21:49:49 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 21:49:49 2021
Terminated at Tue Apr 20 21:45:04 2021
Results reported at Tue Apr 20 21:45:04 2021

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

    CPU time :                                   86033.12 sec.
    Max Memory :                                 3437 MB
    Average Memory :                             3406.41 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12947.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            177896 sec.

The output (if any) is above this job summary.

