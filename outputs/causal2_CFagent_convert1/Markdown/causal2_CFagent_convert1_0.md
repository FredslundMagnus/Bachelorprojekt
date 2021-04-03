
# Parameters

    Name :                      causal2_CFagent_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal2
    Hours :                     13.0
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
    Cf convert :                0
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      30902556362 function calls (30695127927 primitive calls) in 46510.10 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46510.096 46510.096 {built-in method builtins.exec}
                      1    4.571    4.571 46510.096 46510.096 <string>:1(<module>)
                      1  150.615  150.615 46505.525 46505.525 main.py:96(CFagent)
                6813864   26.058    0.000 16585.015    0.002 agent.py:28(learn)
                6813864  427.146    0.000 13491.885    0.002 learner.py:42(Qlearn)
                2271288    9.582    0.000 7847.397    0.003 game.py:36(step)
        232283266/24856522  930.836    0.000 7570.601    0.000 module.py:866(_call_impl)
                2271288   13.762    0.000 7401.984    0.003 layers.py:594(step)
               18042658   48.849    0.000 7073.577    0.000 network.py:24(forward)
               18042658  224.753    0.000 6907.569    0.000 container.py:117(forward)
                2271288  240.838    0.000 6446.630    0.003 agent.py:53(_learn)
                2271288  237.701    0.000 5918.128    0.003 agent.py:189(_learn)
                6813864   57.244    0.000 5289.787    0.001 optimizer.py:84(wrapper)
                6813864   29.249    0.000 5037.065    0.001 grad_mode.py:24(decorate_context)
                6813864  202.390    0.000 4944.012    0.001 adam.py:55(step)
                2271288  191.430    0.000 4883.620    0.002 layers.py:18(step)
                2271288 2719.502    0.001 4813.930    0.002 replaybuffer.py:28(teleporter_save_data)
              226942594  311.256    0.000 4670.146    0.000 layer.py:82(move)
                2271288  327.683    0.000 4519.088    0.002 agent.py:197(counterfact)
                6813864 1054.317    0.000 4515.305    0.001 _functional.py:53(adam)
                2271288   71.246    0.000 4179.412    0.002 agent.py:114(_learn)
                5613954  149.693    0.000 3585.703    0.001 agent.py:48(__call__)
                6813864   27.823    0.000 3485.393    0.001 tensor.py:195(backward)
                6813864   27.873    0.000 3456.565    0.001 __init__.py:68(backward)
                2271288 1957.053    0.001 3399.621    0.001 agent.py:85(interveen)
                6813864 3296.038    0.000 3296.038    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2271288 2389.046    0.001 3166.237    0.001 replaybuffer.py:22(sample_data)
                2271288 2052.407    0.001 2739.165    0.001 replaybuffer.py:49(sample_data)
              226942594  451.113    0.000 2689.200    0.000 layers.py:611(check)
               36085316   86.584    0.000 2554.860    0.000 conv.py:398(forward)
                2271289  239.803    0.000 2485.378    0.001 layers.py:565(update)
               36085316   50.682    0.000 2430.070    0.000 conv.py:390(_conv_forward)
               36085316 2379.389    0.000 2379.389    0.000 {built-in method conv2d}
               29331315 2170.818    0.000 2170.818    0.000 {built-in method tensor}
               23045264   14.752    0.000 2010.741    0.000 game.py:32(board)
               49585398   99.849    0.000 1940.115    0.000 linear.py:93(forward)
               31798039 1075.272    0.000 1917.407    0.000 layer.py:143(NoRock_update)
              195801400 1845.814    0.000 1845.814    0.000 {built-in method clone}
               49585398   43.511    0.000 1790.138    0.000 functional.py:1737(linear)
               49585398 1736.663    0.000 1736.663    0.000 {built-in method torch._C._nn.linear}
                1072264   11.110    0.000 1439.834    0.001 agent.py:167(choose_action)
                2271288  844.650    0.000 1425.877    0.001 agent.py:66(modify)
              226816355  306.162    0.000 1369.956    0.000 layers.py:605(isFree)
               32869410 1222.189    0.000 1222.189    0.000 {built-in method cat}
             1497957071  888.764    0.000 1063.795    0.000 layer.py:79(isFree)
               67628056   63.421    0.000 1052.449    0.000 activation.py:713(forward)
                2271288   38.135    0.000 1014.533    0.000 agent.py:163(__call__)
                7885242   50.800    0.000  992.515    0.000 agent.py:58(modify_board)
               67628056   63.010    0.000  989.028    0.000 functional.py:1364(leaky_relu)
                2271288   35.762    0.000  961.258    0.000 agent.py:109(__call__)
               67628056  914.577    0.000  914.577    0.000 {built-in method torch._C._nn.leaky_relu}
              127192128  873.815    0.000  873.815    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              127192128  776.740    0.000  776.740    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6813864  137.691    0.000  769.189    0.000 optimizer.py:189(zero_grad)
             2749226471  476.460    0.000  694.850    0.000 enum.py:646(__hash__)
                7885242  644.917    0.000  644.917    0.000 {built-in method torch._C._nn.one_hot}
              226942594  389.734    0.000  626.173    0.000 layers.py:217(check)
              227128900   76.447    0.000  617.893    0.000 {built-in method builtins.all}
              226942594  380.925    0.000  616.592    0.000 layers.py:231(check)
              226942594  386.564    0.000  612.288    0.000 layers.py:245(check)
                2271288   45.931    0.000  611.865    0.000 replaybuffer.py:18(stacker)
              714637447  173.084    0.000  567.592    0.000 layers.py:571(<genexpr>)
                1531410   16.285    0.000  540.120    0.000 layers.py:615(restart)
                2271288   45.153    0.000  527.990    0.000 replaybuffer.py:45(stacker)
               63596064  516.479    0.000  516.479    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              598724648  461.779    0.000  461.779    0.000 layer.py:122(elements)
               63596064  451.511    0.000  451.511    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1531410    8.676    0.000  413.470    0.000 level.py:8(__init__)
               63596064  412.719    0.000  412.719    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               63596064  412.594    0.000  412.594    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              205957930  407.296    0.000  407.296    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              227128900  248.743    0.000  370.685    0.000 layers.py:111(isDone)
                2271288  132.194    0.000  358.507    0.000 replaybuffer.py:55(CF_save_data)
              445172532  284.540    0.000  354.891    0.000 tensor.py:906(grad)
                5613954  134.312    0.000  353.402    0.000 exploration.py:53(softmaxer)
                1531410   19.664    0.000  348.093    0.000 levels.py:151(generate)
             3849391941  347.712    0.000  347.712    0.000 layer.py:75(positions)
                2271288  204.792    0.000  346.113    0.000 collector.py:54(collect)
              226942594  219.306    0.000  326.283    0.000 layers.py:204(check)
        4243801390/4243801387  283.562    0.000  325.566    0.000 {built-in method builtins.len}
                4542576  118.669    0.000  316.182    0.000 random.py:315(sample)
                7350323   65.182    0.000  308.782    0.000 level.py:41(notUsed)
               63596064  307.351    0.000  307.351    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6813864   11.513    0.000  290.872    0.000 loss.py:527(forward)
                6813864   27.208    0.000  279.359    0.000 functional.py:2898(mse_loss)
                6813865  260.452    0.000  260.452    0.000 {built-in method nonzero}
                3343552   16.937    0.000  237.982    0.000 exploration.py:47(epsilonGreedy)
             2749252598  218.395    0.000  218.395    0.000 {built-in method builtins.hash}
                1072264  171.786    0.000  212.941    0.000 agent.py:178(convert_values)
              214952487  127.325    0.000  179.021    0.000 layer.py:102(remove)
                6813864  171.151    0.000  171.151    0.000 {built-in method torch._C._nn.mse_loss}
               36085316   25.157    0.000  170.414    0.000 flatten.py:39(forward)
              268215429  125.796    0.000  166.233    0.000 layer.py:106(add)
                6814759  161.196    0.000  161.196    0.000 {built-in method max}
               13627728  147.270    0.000  147.270    0.000 {built-in method sum}
               10157416   14.635    0.000  145.649    0.000 tensor.py:525(__rsub__)
               36085316  145.257    0.000  145.257    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              234548478   95.928    0.000  142.937    0.000 random.py:250(_randbelow_with_getrandbits)
             1497957071  139.490    0.000  139.490    0.000 layer.py:183(isBlocking)
              237899228  130.444    0.000  130.444    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 9493317: <causal2_CFagent_convert1_0> in cluster <dcc> Done

Job <causal2_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:08 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:17:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:17:08 2021
Terminated at Sat Apr  3 11:12:23 2021
Results reported at Sat Apr  3 11:12:23 2021

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

    CPU time :                                   46390.89 sec.
    Max Memory :                                 7794 MB
    Average Memory :                             5663.43 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8590.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46514 sec.
    Turnaround time :                            46935 sec.

The output (if any) is above this job summary.

