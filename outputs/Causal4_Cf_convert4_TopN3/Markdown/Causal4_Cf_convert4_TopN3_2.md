
# Parameters

    Name :                      Causal4_Cf_convert4_TopN3-2
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
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69583280307 function calls (69282088312 primitive calls) in 86110.10 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.098 86110.098 {built-in method builtins.exec}
                      1    4.264    4.264 86110.098 86110.098 <string>:1(<module>)
                      1  352.791  352.791 86105.833 86105.833 main.py:79(CFagent)
                9805230   37.297    0.000 30536.689    0.003 agent.py:29(learn)
                9805230  761.518    0.000 25488.079    0.003 learner.py:42(Qlearn)
                3268410   14.501    0.000 20107.244    0.006 game.py:41(step)
                3268410   20.138    0.000 19293.520    0.006 layers.py:718(step)
        337184196/35993892 1455.097    0.000 13012.457    0.000 module.py:866(_call_impl)
                3268410  308.199    0.000 12874.217    0.004 layers.py:17(step)
              326515066  932.577    0.000 12538.287    0.000 layer.py:98(move)
               26188662   75.914    0.000 12200.405    0.000 network.py:27(forward)
               26188662  386.019    0.000 11949.953    0.000 container.py:117(forward)
                3268410  335.331    0.000 11775.290    0.004 agent.py:54(_learn)
                3268410  331.950    0.000 10913.924    0.003 agent.py:202(_learn)
                9805230   89.553    0.000 10882.548    0.001 optimizer.py:84(wrapper)
                9805230   43.915    0.000 10462.122    0.001 grad_mode.py:24(decorate_context)
                9805230  302.623    0.000 10320.670    0.001 adam.py:55(step)
                3268410  932.930    0.000 10219.261    0.003 agent.py:210(counterfact)
                9805230 2136.782    0.000 9683.735    0.001 _functional.py:53(adam)
              326515066 1558.745    0.000 7831.690    0.000 layers.py:735(check)
                3268410  101.432    0.000 7788.657    0.002 agent.py:117(_learn)
                3268411  481.991    0.000 6374.221    0.002 layers.py:684(update)
                9805230   42.690    0.000 6241.091    0.001 tensor.py:195(backward)
                9805230   39.375    0.000 6196.776    0.001 __init__.py:68(backward)
                8184145  216.566    0.000 6158.931    0.001 agent.py:49(__call__)
                9805230 5931.780    0.001 5931.780    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51478475 5464.709    0.000 5464.709    0.000 {built-in method tensor}
               43950101   29.374    0.000 5241.081    0.000 game.py:37(board)
                3268410 3869.980    0.001 4952.553    0.002 replaybuffer.py:22(sample_data)
                3268410 3699.272    0.001 4755.635    0.001 replaybuffer.py:67(sample_data)
                3268410 1905.251    0.001 4349.772    0.001 agent.py:88(interveen)
               52377324  120.294    0.000 4289.718    0.000 conv.py:398(forward)
               52377324   77.737    0.000 4111.903    0.000 conv.py:390(_conv_forward)
               65368210 2362.516    0.000 4038.053    0.000 layer.py:151(update)
               52377324 4034.165    0.000 4034.165    0.000 {built-in method conv2d}
                3268410 1942.503    0.001 3685.437    0.001 replaybuffer.py:28(teleporter_save_data)
               72029166  156.655    0.000 3459.922    0.000 linear.py:93(forward)
               72029166   62.456    0.000 3224.379    0.000 functional.py:1737(linear)
               72029166 3145.695    0.000 3145.695    0.000 {built-in method torch._C._nn.linear}
              326515066  644.921    0.000 3143.308    0.000 layers.py:729(isFree)
                3268410 1915.204    0.001 2893.357    0.001 agent.py:67(modify)
                1662467   39.865    0.000 2704.364    0.002 agent.py:175(choose_action)
             3149302400 2002.508    0.000 2498.387    0.000 layer.py:95(isFree)
              183030960 1978.618    0.000 1978.618    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               98217828   82.275    0.000 1923.009    0.000 activation.py:713(forward)
               44136655 1856.064    0.000 1856.064    0.000 {built-in method cat}
               98217828   85.909    0.000 1840.734    0.000 functional.py:1364(leaky_relu)
              183030960 1744.284    0.000 1744.284    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               98217828 1736.133    0.000 1736.133    0.000 {built-in method torch._C._nn.leaky_relu}
               11452555   80.282    0.000 1718.905    0.000 agent.py:59(modify_board)
                3268410   55.813    0.000 1715.802    0.001 agent.py:171(__call__)
              124134055 1705.147    0.000 1705.147    0.000 {built-in method clone}
                3268410   54.480    0.000 1600.734    0.000 agent.py:112(__call__)
             6097913948 1102.307    0.000 1583.488    0.000 enum.py:646(__hash__)
                9805230  252.294    0.000 1524.467    0.000 optimizer.py:189(zero_grad)
              327042795  334.922    0.000 1509.445    0.000 {built-in method builtins.any}
                3268410 1055.760    0.000 1363.726    0.000 replaybuffer.py:73(CF_save_data)
              326515066  966.965    0.000 1265.409    0.000 layers.py:77(check)
             3561518224  982.978    0.000 1174.523    0.000 layers.py:700(<genexpr>)
                3066716   38.354    0.000 1123.589    0.000 layers.py:740(restart)
              326515066  718.030    0.000 1110.039    0.000 layers.py:246(check)
               11452555 1093.981    0.000 1093.981    0.000 {built-in method torch._C._nn.one_hot}
               91515480 1084.405    0.000 1084.405    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              326515066  624.568    0.000 1020.291    0.000 layers.py:286(check)
              326841100  187.310    0.000  963.835    0.000 {built-in method builtins.all}
               91515480  933.218    0.000  933.218    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1062009461  925.591    0.000  925.591    0.000 layer.py:146(elements)
               91515480  892.128    0.000  892.128    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91515480  884.393    0.000  884.393    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3268410   64.430    0.000  842.028    0.000 replaybuffer.py:18(stacker)
                3268410   64.537    0.000  823.889    0.000 replaybuffer.py:63(stacker)
             2041978196  519.789    0.000  815.198    0.000 layers.py:690(<genexpr>)
                3066716   17.126    0.000  791.545    0.000 level.py:8(__init__)
             7968660255  716.505    0.000  716.505    0.000 layer.py:91(positions)
                3268410  427.918    0.000  706.105    0.000 collector.py:46(collect)
               91515480  693.178    0.000  693.178    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              326515066  497.885    0.000  654.950    0.000 layers.py:62(check)
                3066716  103.055    0.000  639.302    0.000 levels.py:199(generate)
        8607394994/8607394991  571.713    0.000  639.116    0.000 {built-in method builtins.len}
                8184145  232.902    0.000  630.513    0.000 exploration.py:53(softmaxer)
              326515066  366.671    0.000  565.800    0.000 layers.py:273(check)
              640608444  452.230    0.000  557.719    0.000 tensor.py:906(grad)
                1662467  465.991    0.000  550.306    0.000 agent.py:186(convert_values)
              326515066  345.393    0.000  535.329    0.000 layers.py:313(check)
               12670252  192.764    0.000  510.602    0.000 random.py:315(sample)
                9805230   16.685    0.000  495.168    0.000 loss.py:527(forward)
             6097951163  481.187    0.000  481.187    0.000 {built-in method builtins.hash}
                9805230   37.244    0.000  478.483    0.000 functional.py:2898(mse_loss)
              138855020  449.772    0.000  449.772    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              326515066  301.242    0.000  446.852    0.000 layers.py:48(check)
                6133432   50.683    0.000  434.174    0.000 level.py:41(notUsed)
              326515066  247.025    0.000  359.180    0.000 layers.py:23(check)
               52377324   47.242    0.000  326.489    0.000 flatten.py:39(forward)
                9805230  314.217    0.000  314.217    0.000 {built-in method torch._C._nn.mse_loss}
               19610460  295.564    0.000  295.564    0.000 {built-in method sum}
             3604460218  287.509    0.000  287.509    0.000 {method 'random' of '_random.Random' objects}
              282771258  208.614    0.000  285.298    0.000 layer.py:126(remove)
               30667160   41.306    0.000  283.495    0.000 layer.py:69(restart)
                6536822  282.495    0.000  282.495    0.000 {built-in method nonzero}
                9806374  280.251    0.000  280.251    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551820: <Causal4_Cf_convert4_TopN3_2> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 06:29:03 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 06:29:03 2021
Terminated at Sat Apr 24 06:24:18 2021
Results reported at Sat Apr 24 06:24:18 2021

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

    CPU time :                                   85898.31 sec.
    Max Memory :                                 9413 MB
    Average Memory :                             6340.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6971.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            270226 sec.

The output (if any) is above this job summary.

