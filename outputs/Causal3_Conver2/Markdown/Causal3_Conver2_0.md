
# Parameters

    Name :                      Causal3_Conver2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      70446904696 function calls (70085435189 primitive calls) in 86113.12 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.119 86113.119 {built-in method builtins.exec}
                      1    4.212    4.212 86113.119 86113.119 <string>:1(<module>)
                      1  382.935  382.935 86108.906 86108.906 main.py:79(CFagent)
               11248875   41.432    0.000 27066.368    0.002 agent.py:29(learn)
               11248873  690.116    0.000 22072.033    0.002 learner.py:42(Qlearn)
                3749625   16.654    0.000 19090.578    0.005 game.py:41(step)
                3749625   20.119    0.000 18316.260    0.005 layers.py:718(step)
        404088882/42621066 1581.574    0.000 12972.290    0.000 module.py:866(_call_impl)
               31372193   88.299    0.000 12152.395    0.000 network.py:27(forward)
               31372193  395.126    0.000 11871.739    0.000 container.py:117(forward)
                3749625  325.307    0.000 11304.296    0.003 layers.py:17(step)
              374911242  627.140    0.000 10940.756    0.000 layer.py:98(move)
                3749625  370.280    0.000 10514.924    0.003 agent.py:54(_learn)
                3749625 1025.041    0.000 10019.629    0.003 agent.py:212(counterfact)
                3749625  365.984    0.000 9651.873    0.003 agent.py:204(_learn)
               11248873   97.311    0.000 8718.460    0.001 optimizer.py:84(wrapper)
               11248873   47.513    0.000 8298.566    0.001 grad_mode.py:24(decorate_context)
               11248873  332.358    0.000 8150.091    0.001 adam.py:55(step)
               11248873 1720.831    0.000 7442.164    0.001 _functional.py:53(adam)
                3749626  535.827    0.000 6963.839    0.002 layers.py:684(update)
                3749625  112.129    0.000 6834.139    0.002 agent.py:117(_learn)
              374911242 1458.040    0.000 6536.993    0.000 layers.py:735(check)
               10060022  258.396    0.000 6370.431    0.001 agent.py:49(__call__)
                3749625 3424.071    0.001 6073.480    0.002 replaybuffer.py:28(teleporter_save_data)
                3749625 4553.152    0.001 5659.520    0.002 replaybuffer.py:22(sample_data)
               11248873   43.477    0.000 5617.760    0.000 tensor.py:195(backward)
               11248873   41.456    0.000 5572.715    0.000 __init__.py:68(backward)
                3749625 4383.955    0.001 5460.529    0.001 replaybuffer.py:67(sample_data)
                3749625 2994.386    0.001 5359.163    0.001 agent.py:88(interveen)
               11248873 5309.879    0.000 5309.879    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53923635 4573.301    0.000 4573.301    0.000 {built-in method tensor}
               62744386  145.074    0.000 4408.060    0.000 conv.py:398(forward)
               45332041   28.761    0.000 4370.397    0.000 game.py:37(board)
               62744386   97.878    0.000 4204.072    0.000 conv.py:390(_conv_forward)
               62744386 4106.194    0.000 4106.194    0.000 {built-in method conv2d}
               59994008 1995.331    0.000 3577.245    0.000 layer.py:167(NoRock_update)
                2564050   51.531    0.000 3407.733    0.001 agent.py:176(choose_action)
               86617329  168.962    0.000 3317.258    0.000 linear.py:93(forward)
              374911242  750.573    0.000 3197.683    0.000 layers.py:729(isFree)
               86617329   73.130    0.000 3064.795    0.000 functional.py:1737(linear)
               86617329 2974.492    0.000 2974.492    0.000 {built-in method torch._C._nn.linear}
                3749625 1834.576    0.000 2745.682    0.001 agent.py:67(modify)
              263572345 2527.894    0.000 2527.894    0.000 {built-in method clone}
             2894233021 1997.809    0.000 2447.110    0.000 layer.py:95(isFree)
               51305887 1841.848    0.000 1841.848    0.000 {built-in method cat}
              117989522   92.827    0.000 1808.160    0.000 activation.py:713(forward)
               13809647   89.519    0.000 1766.447    0.000 agent.py:59(modify_board)
              117989522  102.460    0.000 1715.333    0.000 functional.py:1364(leaky_relu)
                5271742   53.972    0.000 1670.891    0.000 layers.py:740(restart)
                3749623   58.910    0.000 1646.334    0.000 agent.py:172(__call__)
              117989522 1593.926    0.000 1593.926    0.000 {built-in method torch._C._nn.leaky_relu}
                3749625 1213.955    0.000 1578.466    0.000 replaybuffer.py:73(CF_save_data)
                3749625   56.223    0.000 1553.280    0.000 agent.py:112(__call__)
             5654313221 1041.145    0.000 1490.024    0.000 enum.py:646(__hash__)
              209978960 1449.141    0.000 1449.141    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              373440484  328.759    0.000 1396.492    0.000 {built-in method builtins.any}
              374911242  868.841    0.000 1388.413    0.000 layers.py:286(check)
              374962600  203.896    0.000 1314.907    0.000 {built-in method builtins.all}
               11248873  228.987    0.000 1303.791    0.000 optimizer.py:189(zero_grad)
              209978960 1287.489    0.000 1287.489    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              374911242  742.891    0.000 1250.544    0.000 layers.py:246(check)
                5271742   27.524    0.000 1175.647    0.000 level.py:8(__init__)
             2102981297  536.653    0.000 1156.717    0.000 layers.py:690(<genexpr>)
               13809647 1156.447    0.000 1156.447    0.000 {built-in method torch._C._nn.one_hot}
             3327217722  883.866    0.000 1067.733    0.000 layers.py:700(<genexpr>)
                5271742  106.445    0.000  933.069    0.000 levels.py:164(generate)
             1378419001  884.445    0.000  884.445    0.000 layer.py:146(elements)
              104989480  863.666    0.000  863.666    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3749625   62.598    0.000  838.278    0.000 replaybuffer.py:18(stacker)
                3749623   65.341    0.000  816.025    0.000 replaybuffer.py:63(stacker)
              104989480  743.272    0.000  743.272    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              104989480  680.757    0.000  680.757    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10543484   99.231    0.000  679.849    0.000 level.py:41(notUsed)
             7222991337  679.283    0.000  679.283    0.000 layer.py:91(positions)
              104989480  670.330    0.000  670.330    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        8435299133/8435299130  577.810    0.000  648.771    0.000 {built-in method builtins.len}
                2564050  564.958    0.000  635.944    0.000 agent.py:187(convert_values)
               10060022  240.739    0.000  632.294    0.000 exploration.py:53(softmaxer)
              374911242  389.212    0.000  624.004    0.000 layers.py:313(check)
               18042734  236.247    0.000  618.322    0.000 random.py:315(sample)
              374911242  389.662    0.000  615.821    0.000 layers.py:273(check)
              734926444  482.949    0.000  600.833    0.000 tensor.py:906(grad)
                3749625  333.963    0.000  569.424    0.000 collector.py:46(collect)
              281131615  548.095    0.000  548.095    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              104989480  523.138    0.000  523.138    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              374911242  331.149    0.000  498.474    0.000 layers.py:48(check)
               11248873   17.340    0.000  475.174    0.000 loss.py:527(forward)
               11248873   41.860    0.000  457.834    0.000 functional.py:2898(mse_loss)
             5654355812  448.888    0.000  448.888    0.000 {built-in method builtins.hash}
               42173936   51.996    0.000  427.126    0.000 layer.py:69(restart)
              374911242  266.405    0.000  403.699    0.000 layers.py:23(check)
              216545574  265.705    0.000  394.016    0.000 layers.py:113(isDone)
              631570486  262.293    0.000  360.400    0.000 layer.py:130(add)
              510640621  228.013    0.000  332.614    0.000 random.py:250(_randbelow_with_getrandbits)
              365435590  218.714    0.000  314.460    0.000 layer.py:126(remove)
               62744386   47.649    0.000  298.276    0.000 flatten.py:39(forward)
               11248873  281.518    0.000  281.518    0.000 {built-in method torch._C._nn.mse_loss}
                7499252  277.225    0.000  277.225    0.000 {built-in method nonzero}
                5271842  138.639    0.000  273.751    0.000 layers.py:36(reset)
               10543484   11.295    0.000  271.225    0.000 level.py:38(elementsIn)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579157: <Causal3_Conver2_0> in cluster <dcc> Done

Job <Causal3_Conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:05 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 05:40:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 05:40:27 2021
Terminated at Wed Apr 28 05:35:47 2021
Results reported at Wed Apr 28 05:35:47 2021

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

    CPU time :                                   85901.80 sec.
    Max Memory :                                 10603 MB
    Average Memory :                             7017.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5781.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            96702 sec.

The output (if any) is above this job summary.

