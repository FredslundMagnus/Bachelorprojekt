
# Parameters

    Name :                      Causal4_Cf_convert4_TopN6-1
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


      80142977971 function calls (79797851588 primitive calls) in 86109.49 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.489 86109.489 {built-in method builtins.exec}
                      1    4.258    4.258 86109.489 86109.489 <string>:1(<module>)
                      1  378.888  378.888 86105.230 86105.230 main.py:79(CFagent)
               11127186   39.847    0.000 26778.045    0.002 agent.py:29(learn)
                3709062   15.585    0.000 23062.814    0.006 game.py:41(step)
                3709062   18.840    0.000 22227.074    0.006 layers.py:718(step)
               11127171  666.125    0.000 21818.327    0.002 learner.py:42(Qlearn)
                3709062  328.101    0.000 14387.418    0.004 layers.py:17(step)
              370607949 1065.994    0.000 14027.326    0.000 layer.py:98(move)
        386248608/41123916 1523.050    0.000 12417.937    0.000 module.py:866(_call_impl)
               29996745   85.768    0.000 11614.729    0.000 network.py:27(forward)
               29996745  382.932    0.000 11342.530    0.000 container.py:117(forward)
                3709062  952.305    0.000 10862.089    0.003 agent.py:210(counterfact)
                3709062  372.924    0.000 10387.741    0.003 agent.py:54(_learn)
                3709062  367.648    0.000 9552.536    0.003 agent.py:202(_learn)
              370607949 1695.169    0.000 8868.915    0.000 layers.py:735(check)
               11127171   91.515    0.000 8663.216    0.001 optimizer.py:84(wrapper)
               11127171   46.496    0.000 8246.074    0.001 grad_mode.py:24(decorate_context)
               11127171  326.351    0.000 8097.532    0.001 adam.py:55(step)
                3709063  541.127    0.000 7792.378    0.002 layers.py:684(update)
               11127171 1711.255    0.000 7403.690    0.001 _functional.py:53(adam)
                3709062  112.891    0.000 6772.043    0.002 agent.py:117(_learn)
                9427271  236.288    0.000 5963.022    0.001 agent.py:49(__call__)
               59023787 5884.448    0.000 5884.448    0.000 {built-in method tensor}
               50521775   32.435    0.000 5687.095    0.000 game.py:37(board)
                3709062 4558.242    0.001 5666.416    0.002 replaybuffer.py:22(sample_data)
               11127171   43.131    0.000 5560.306    0.000 tensor.py:195(backward)
               11127171   43.021    0.000 5515.705    0.000 __init__.py:68(backward)
                3709062 4339.840    0.001 5411.150    0.001 replaybuffer.py:67(sample_data)
               11127171 5254.352    0.000 5254.352    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               74181250 2630.921    0.000 4537.690    0.000 layer.py:151(update)
               59993490  132.368    0.000 4205.924    0.000 conv.py:398(forward)
               59993490   76.017    0.000 4006.704    0.000 conv.py:390(_conv_forward)
                3709062 1674.957    0.000 4002.418    0.001 agent.py:88(interveen)
               59993490 3930.687    0.000 3930.687    0.000 {built-in method conv2d}
              370607949  685.046    0.000 3377.633    0.000 layers.py:729(isFree)
                3709062 1831.457    0.000 3269.166    0.001 replaybuffer.py:28(teleporter_save_data)
               82572111  162.044    0.000 3180.789    0.000 linear.py:93(forward)
               82572111   68.133    0.000 2934.095    0.000 functional.py:1737(linear)
               82572111 2850.082    0.000 2850.082    0.000 {built-in method torch._C._nn.linear}
                2024194   43.091    0.000 2706.350    0.001 agent.py:175(choose_action)
             3330638278 2157.435    0.000 2692.587    0.000 layer.py:95(isFree)
                3709062 1751.047    0.000 2661.115    0.001 agent.py:67(modify)
             7324558096 1358.680    0.000 1941.740    0.000 enum.py:646(__hash__)
               50226878 1815.645    0.000 1815.645    0.000 {built-in method cat}
              112568856   92.096    0.000 1700.861    0.000 activation.py:713(forward)
              370626523  381.377    0.000 1699.614    0.000 {built-in method builtins.any}
               13136333   86.451    0.000 1684.623    0.000 agent.py:59(modify_board)
                3709047   59.183    0.000 1639.810    0.000 agent.py:171(__call__)
              112568856   94.568    0.000 1608.764    0.000 functional.py:1364(leaky_relu)
                3709062   57.185    0.000 1530.500    0.000 agent.py:112(__call__)
              370906300  217.495    0.000 1510.859    0.000 {built-in method builtins.all}
              112568856 1496.493    0.000 1496.493    0.000 {built-in method torch._C._nn.leaky_relu}
              148035419 1464.960    0.000 1464.960    0.000 {built-in method clone}
                3988840   47.498    0.000 1448.888    0.000 layers.py:740(restart)
              207707172 1442.067    0.000 1442.067    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              370607949 1032.103    0.000 1369.589    0.000 layers.py:77(check)
             2248001635  580.512    0.000 1339.311    0.000 layers.py:690(<genexpr>)
             4036092060 1083.484    0.000 1318.237    0.000 layers.py:700(<genexpr>)
                3709062 1029.884    0.000 1314.019    0.000 replaybuffer.py:73(CF_save_data)
              370607949  853.555    0.000 1312.745    0.000 layers.py:286(check)
              207707172 1293.897    0.000 1293.897    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11127171  222.062    0.000 1255.888    0.000 optimizer.py:189(zero_grad)
              370607949  713.111    0.000 1167.809    0.000 layers.py:246(check)
               13136333 1104.876    0.000 1104.876    0.000 {built-in method torch._C._nn.one_hot}
             1265738939 1053.426    0.000 1053.426    0.000 layer.py:146(elements)
                3988840   21.293    0.000 1024.867    0.000 level.py:8(__init__)
             9584493358  892.122    0.000  892.122    0.000 layer.py:91(positions)
              103853586  842.577    0.000  842.577    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3709062   65.068    0.000  838.505    0.000 replaybuffer.py:18(stacker)
                3988840  134.357    0.000  829.477    0.000 levels.py:199(generate)
                3709047   65.155    0.000  811.244    0.000 replaybuffer.py:63(stacker)
              370607949  548.351    0.000  721.974    0.000 layers.py:62(check)
              103853586  721.893    0.000  721.893    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        9781560712/9781560709  634.549    0.000  701.476    0.000 {built-in method builtins.len}
              103853586  686.463    0.000  686.463    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              370607949  447.789    0.000  682.536    0.000 layers.py:313(check)
              103853586  676.227    0.000  676.227    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              370607949  442.583    0.000  666.407    0.000 layers.py:273(check)
              370906300  435.492    0.000  657.995    0.000 layers.py:113(isDone)
             7324600239  583.068    0.000  583.068    0.000 {built-in method builtins.hash}
               15395804  220.215    0.000  582.126    0.000 random.py:315(sample)
                9427271  219.460    0.000  581.544    0.000 exploration.py:53(softmaxer)
              726975186  459.587    0.000  572.924    0.000 tensor.py:906(grad)
                3709062  335.548    0.000  566.726    0.000 collector.py:46(collect)
                7977680   66.728    0.000  562.261    0.000 level.py:41(notUsed)
                2024194  442.275    0.000  519.314    0.000 agent.py:186(convert_values)
              103853586  510.410    0.000  510.410    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              370607949  332.599    0.000  491.930    0.000 layers.py:48(check)
               11127171   15.203    0.000  468.036    0.000 loss.py:527(forward)
               11127171   41.721    0.000  452.834    0.000 functional.py:2898(mse_loss)
              370607949  280.669    0.000  406.609    0.000 layers.py:23(check)
               39888400   52.542    0.000  363.175    0.000 layer.py:69(restart)
              164880799  335.049    0.000  335.049    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             4092661272  328.099    0.000  328.099    0.000 {method 'random' of '_random.Random' objects}
              559594116  233.743    0.000  314.765    0.000 layer.py:130(add)
              323537885  219.384    0.000  307.490    0.000 layer.py:126(remove)
              447757186  199.994    0.000  291.050    0.000 random.py:250(_randbelow_with_getrandbits)
               59993490   44.004    0.000  279.108    0.000 flatten.py:39(forward)
               11127171  278.391    0.000  278.391    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533965: <Causal4_Cf_convert4_TopN6_1> in cluster <dcc> Done

Job <Causal4_Cf_convert4_TopN6_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 22:01:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 22:01:31 2021
Terminated at Tue Apr 20 21:56:45 2021
Results reported at Tue Apr 20 21:56:45 2021

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

    CPU time :                                   85905.14 sec.
    Max Memory :                                 10324 MB
    Average Memory :                             6816.07 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6060.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            178597 sec.

The output (if any) is above this job summary.

