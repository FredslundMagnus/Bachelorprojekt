
# Parameters

    Name :                      Causal4_Cf_convert5_TopN6-0
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
    Cf convert :                5
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63297245062 function calls (63009990443 primitive calls) in 86118.39 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.391 86118.391 {built-in method builtins.exec}
                      1    5.975    5.975 86118.391 86118.391 <string>:1(<module>)
                      1  445.246  445.246 86112.416 86112.416 main.py:79(CFagent)
                9443223   49.437    0.000 26462.800    0.003 agent.py:29(learn)
                9443222  706.116    0.000 21138.250    0.002 learner.py:42(Qlearn)
                3147741   19.471    0.000 20346.118    0.006 game.py:41(step)
                3147741   22.413    0.000 19474.652    0.006 layers.py:718(step)
                3147741  317.050    0.000 13289.792    0.004 layers.py:17(step)
              314360448  968.746    0.000 12942.412    0.000 layer.py:98(move)
        321683141/34430213 1480.789    0.000 12013.748    0.000 module.py:866(_call_impl)
               24986991   80.570    0.000 11132.647    0.000 network.py:27(forward)
               24986991  373.728    0.000 10862.202    0.000 container.py:117(forward)
                3147741  441.987    0.000 10307.676    0.003 agent.py:54(_learn)
                3147741  810.019    0.000 9936.572    0.003 agent.py:210(counterfact)
                3147741  435.747    0.000 9327.161    0.003 agent.py:202(_learn)
                9443222  118.316    0.000 7966.887    0.001 optimizer.py:84(wrapper)
                3147741 6716.107    0.002 7918.217    0.003 replaybuffer.py:22(sample_data)
              314360448 1544.478    0.000 7878.728    0.000 layers.py:735(check)
                3147741 6383.446    0.002 7517.586    0.002 replaybuffer.py:67(sample_data)
                9443222   57.649    0.000 7472.810    0.001 grad_mode.py:24(decorate_context)
                9443222  335.669    0.000 7288.044    0.001 adam.py:55(step)
                3147741  121.875    0.000 6754.704    0.002 agent.py:117(_learn)
                9443222 1526.988    0.000 6598.280    0.001 _functional.py:53(adam)
                3147742  496.449    0.000 6125.327    0.002 layers.py:684(update)
                7765155  285.484    0.000 5962.821    0.001 agent.py:49(__call__)
                9443222   49.840    0.000 5687.919    0.001 tensor.py:195(backward)
                9443222   54.398    0.000 5636.553    0.001 __init__.py:68(backward)
               49170858 5392.722    0.000 5392.722    0.000 {built-in method tensor}
                9443222 5338.414    0.001 5338.414    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               41908926   30.205    0.000 5188.301    0.000 game.py:37(board)
               62954830 2895.050    0.000 4988.407    0.000 layer.py:151(update)
               49973982  123.502    0.000 4141.214    0.000 conv.py:398(forward)
                3147741 1627.194    0.001 3975.306    0.001 agent.py:88(interveen)
               49973982   93.953    0.000 3956.013    0.000 conv.py:390(_conv_forward)
               49973982 3862.060    0.000 3862.060    0.000 {built-in method conv2d}
              314360448  593.656    0.000 3427.741    0.000 layers.py:729(isFree)
                3147741 1786.400    0.001 3090.073    0.001 replaybuffer.py:28(teleporter_save_data)
               68665491  152.504    0.000 3055.158    0.000 linear.py:93(forward)
             2669746279 2373.305    0.000 2834.086    0.000 layer.py:95(isFree)
               68665491   62.673    0.000 2819.202    0.000 functional.py:1737(linear)
               68665491 2741.978    0.000 2741.978    0.000 {built-in method torch._C._nn.linear}
                3147741 1733.547    0.001 2709.639    0.001 agent.py:67(modify)
                1483133   36.857    0.000 2161.237    0.001 agent.py:175(choose_action)
               42390301 1898.928    0.000 1898.928    0.000 {built-in method cat}
               10912896   98.193    0.000 1732.952    0.000 agent.py:59(modify_board)
                3147740   75.931    0.000 1686.700    0.001 agent.py:171(__call__)
             5820617174 1107.920    0.000 1562.896    0.000 enum.py:646(__hash__)
               93652482   87.031    0.000 1549.412    0.000 activation.py:713(forward)
                3147741   71.513    0.000 1479.975    0.000 agent.py:112(__call__)
               93652482   90.770    0.000 1462.380    0.000 functional.py:1364(leaky_relu)
              315269039  331.392    0.000 1418.397    0.000 {built-in method builtins.any}
               93652482 1355.502    0.000 1355.502    0.000 {built-in method torch._C._nn.leaky_relu}
              120731512 1296.467    0.000 1296.467    0.000 {built-in method clone}
              985449311 1280.905    0.000 1280.905    0.000 layer.py:146(elements)
              314360448  965.830    0.000 1276.872    0.000 layers.py:77(check)
              176273476 1266.324    0.000 1266.324    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              314360448  775.840    0.000 1171.600    0.000 layers.py:286(check)
               10912896 1141.735    0.000 1141.735    0.000 {built-in method torch._C._nn.one_hot}
                3147741  905.693    0.000 1126.790    0.000 replaybuffer.py:73(CF_save_data)
                9443222  207.132    0.000 1123.033    0.000 optimizer.py:189(zero_grad)
              176273476 1116.392    0.000 1116.392    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             3433334267  894.720    0.000 1087.005    0.000 layers.py:700(<genexpr>)
                2652903   37.911    0.000 1067.438    0.000 layers.py:740(restart)
              314360448  609.804    0.000  987.899    0.000 layers.py:246(check)
                3147741   77.598    0.000  914.714    0.000 replaybuffer.py:18(stacker)
                3147740   77.029    0.000  858.310    0.000 replaybuffer.py:63(stacker)
                2652903   17.814    0.000  755.945    0.000 level.py:8(__init__)
               88136738  745.111    0.000  745.111    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              314360448  582.858    0.000  726.183    0.000 layers.py:62(check)
             7547334609  691.890    0.000  691.890    0.000 layer.py:91(positions)
               88136738  661.502    0.000  661.502    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8339703408/8339703405  564.969    0.000  635.946    0.000 {built-in method builtins.len}
                7765155  222.013    0.000  633.583    0.000 exploration.py:53(softmaxer)
               88136738  632.971    0.000  632.971    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               88136738  621.603    0.000  621.603    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11601288  229.489    0.000  600.213    0.000 random.py:315(sample)
                2652903   98.030    0.000  592.042    0.000 levels.py:199(generate)
                9443222   23.166    0.000  535.041    0.000 loss.py:527(forward)
              616957250  425.984    0.000  527.178    0.000 tensor.py:906(grad)
              314360448  335.198    0.000  523.414    0.000 layers.py:273(check)
              314360448  328.104    0.000  517.699    0.000 layers.py:313(check)
                9443222   54.929    0.000  511.875    0.000 functional.py:2898(mse_loss)
                3147741  296.741    0.000  511.529    0.000 collector.py:46(collect)
              314360448  331.464    0.000  476.327    0.000 layers.py:48(check)
             5820653045  454.983    0.000  454.983    0.000 {built-in method builtins.hash}
               88136738  440.302    0.000  440.302    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5305806   47.584    0.000  396.546    0.000 level.py:41(notUsed)
              314774200   65.675    0.000  391.781    0.000 {built-in method builtins.all}
              696238636  160.801    0.000  365.882    0.000 layers.py:690(<genexpr>)
                1483133  325.989    0.000  346.445    0.000 agent.py:186(convert_values)
              314360448  230.186    0.000  343.788    0.000 layers.py:23(check)
                9443222  305.211    0.000  305.211    0.000 {built-in method torch._C._nn.mse_loss}
              134792148  295.837    0.000  295.837    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6295484  293.948    0.000  293.948    0.000 {built-in method nonzero}
               62954830  285.345    0.000  285.345    0.000 layer.py:163(<listcomp>)
              269999497  203.752    0.000  284.824    0.000 layer.py:126(remove)
             3469485030  284.147    0.000  284.147    0.000 {method 'random' of '_random.Random' objects}
                9444312  270.293    0.000  270.293    0.000 {built-in method max}
              371767339  178.235    0.000  270.200    0.000 random.py:250(_randbelow_with_getrandbits)
              430271015  195.235    0.000  269.538    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533967: <Causal4_Cf_convert5_TopN6_0> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 01:43:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 01:43:12 2021
Terminated at Thu Apr 22 01:38:40 2021
Results reported at Thu Apr 22 01:38:40 2021

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

    CPU time :                                   85907.85 sec.
    Max Memory :                                 9421 MB
    Average Memory :                             6298.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6963.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            278312 sec.

The output (if any) is above this job summary.

